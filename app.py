from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datetime import datetime
import os

app = Flask(__name__)


API_KEY = "AIzaSyA6pRaW3lX6QL1J3e7ywhk0qCpF3QYvhcI"  
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel('gemini-2.0-flash')


SYSTEM_PROMPT = """You are MediMate, an AI medical assistant that specializes in recommending the right medical specialists based on symptoms and health concerns. Your primary role is to:

1. Listen to users' symptoms and health concerns
2. Recommend the most appropriate medical specialist(s) to consult
3. Provide brief, helpful information about the condition
4. Explain why that particular specialist is recommended
5. Always emphasize the importance of professional medical consultation

Guidelines:
- Be empathetic and supportive
- Provide clear, easy-to-understand explanations
- Always recommend seeking professional medical help
- If symptoms sound urgent, advise immediate medical attention
- Include common specialist types like: Cardiologist, Dermatologist, Neurologist, Orthopedist, Gastroenterologist, Pulmonologist, Endocrinologist, Rheumatologist, Psychiatrist, Gynecologist, Urologist, Ophthalmologist, ENT Specialist, etc.
- Keep responses concise but informative
- Never provide specific medical diagnoses, only specialist recommendations

Format your responses to include:
- Acknowledgment of their concern
- Recommended specialist(s)
- Brief explanation of why
- General advice about the condition
- Reminder to seek professional help

Remember: You're helping people find the right medical professional, not replacing medical advice."""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
    
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\n\nMediMate:"
        
        
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=150,
                temperature=0.7
            )
        )
        
        bot_response = response.text
        newtext = ""
        for i in range(len(bot_response)):
            if bot_response[i] == "*":
                continue
            else:
                newtext+=bot_response[i]
        
        return jsonify({
            'response': newtext,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        error_message = str(e)
        print(f"Error occurred: {error_message}") 
        
        if 'API_KEY_INVALID' in error_message or 'invalid API key' in error_message.lower():
            return jsonify({'error': 'Google Gemini API authentication failed. Please check your API key.'}), 500
        elif 'quota' in error_message.lower() or 'rate limit' in error_message.lower():
            return jsonify({'error': 'Rate limit or quota exceeded. Please try again later.'}), 429
        elif 'blocked' in error_message.lower():
            return jsonify({'error': 'Content was blocked by safety filters. Please rephrase your message.'}), 400
        else:
            return jsonify({'error': f'An unexpected error occurred: {error_message}'}), 500

#returns the website is working or not
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'service': 'MediMate'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)