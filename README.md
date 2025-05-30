# MediMate - AI Medical Specialist Recommendation System

MediMate is an AI-powered Flask web application that helps users find the right medical specialists based on their symptoms and health concerns. Using Google's Gemini AI, it provides personalized specialist recommendations and helpful medical guidance.

## 🚀 Features

- **Intelligent Specialist Matching**: AI-powered recommendations for appropriate medical specialists
- **Symptom Analysis**: Analyzes user-described symptoms to suggest relevant specialties
- **Educational Information**: Provides brief, helpful information about medical conditions
- **Safety-First Approach**: Always emphasizes the importance of professional medical consultation
- **REST API**: Simple JSON-based API for chat interactions
- **Health Check Endpoint**: Monitor application status

## 🏥 Supported Medical Specialties

- Cardiologist (Heart conditions)
- Dermatologist (Skin conditions)
- Neurologist (Nervous system)
- Orthopedist (Bone and joint issues)
- Gastroenterologist (Digestive system)
- Pulmonologist (Respiratory system)
- Endocrinologist (Hormonal disorders)
- Rheumatologist (Autoimmune conditions)
- Psychiatrist (Mental health)
- Gynecologist (Women's health)
- Urologist (Urinary system)
- Ophthalmologist (Eye care)
- ENT Specialist (Ear, Nose, Throat)
- And many more...

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd medimate
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (Recommended)
   
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

5. **Configure API Key**
   
   Option 1: Update the API key directly in `app.py` (not recommended for production)
   ```python
   API_KEY = "your_actual_api_key_here"
   ```
   
   Option 2: Use environment variables (recommended)
   ```python
   API_KEY = os.getenv('GEMINI_API_KEY')
   ```


## 🏃‍♂️ Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your browser and go to: `http://localhost:5000`
   - The API will be available at: `http://localhost:5000/chat`
   - Health check endpoint: `http://localhost:5000/health`

## 📁 Project Structure

```
medimate/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore file
│
└── templates/           # HTML templates (you need to create this)
    └── index.html       # Frontend interface
```

## 🌐 API Endpoints

### POST /chat
Send a message to MediMate and get specialist recommendations.

**Request:**
```json
{
  "message": "I have been experiencing chest pain and shortness of breath"
}
```

**Response:**
```json
{
  "response": "I understand your concern about chest pain and shortness of breath. Based on these symptoms, I recommend consulting with a **Cardiologist** as your primary specialist...",
  "timestamp": "2024-05-30T10:30:00.000000"
}
```

### GET /health
Check if the application is running properly.

**Response:**
```json
{
  "status": "healthy",
  "service": "MediMate"
}
```

## 🖥️ Frontend Template

Create a `templates/index.html` file for the web interface:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediMate - Medical Specialist Finder</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
        .chat-box { border: 1px solid #ddd; height: 400px; overflow-y: scroll; padding: 20px; margin: 20px 0; }
        .input-group { display: flex; gap: 10px; }
        #messageInput { flex: 1; padding: 10px; }
        #sendButton { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏥 MediMate - Medical Specialist Finder</h1>
        <p>Describe your symptoms and get recommendations for the right medical specialist.</p>
        
        <div id="chatBox" class="chat-box"></div>
        
        <div class="input-group">
            <input type="text" id="messageInput" placeholder="Describe your symptoms..." />
            <button id="sendButton">Send</button>
        </div>
    </div>

    <script>
        // Add your JavaScript for chat functionality here
    </script>
</body>
</html>
```

## ⚠️ Important Disclaimers

- **Not a Medical Diagnosis Tool**: MediMate provides specialist recommendations only
- **Emergency Situations**: For urgent symptoms, seek immediate medical attention
- **Professional Consultation**: Always consult with qualified healthcare professionals
- **Educational Purpose**: Information provided is for educational purposes only

## 🔧 Configuration Options

### Generation Parameters
You can modify the AI response behavior in `app.py`:

```python
generation_config=genai.types.GenerationConfig(
    max_output_tokens=600,    # Adjust response length
    temperature=0.7           # Adjust creativity (0.0-1.0)
)
```

### Error Handling
The application handles various error scenarios:
- Invalid API keys
- Rate limiting
- Content safety filters
- Network issues

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider:
- Using a WSGI server like Gunicorn
- Setting up proper environment variables
- Implementing rate limiting
- Adding authentication if needed
- Using HTTPS

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues:

1. **API Key Error**
   - Verify your Gemini API key is correct
   - Check if the API key has proper permissions
   - Ensure you haven't exceeded rate limits

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify you're using the correct Python version

3. **Template Not Found**
   - Create the `templates/` directory
   - Add the `index.html` file in the templates folder

4. **Port Already in Use**
   - Change the port in `app.py`: `app.run(port=5001)`
   - Or kill the process using the port

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the error messages in the console
3. Ensure all prerequisites are met
4. Verify your API key is working

---

**Remember: MediMate is a tool to help you find the right medical professional. It does not replace professional medical advice, diagnosis, or treatment.**
