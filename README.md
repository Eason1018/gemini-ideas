# Gemini Ideas App

This is a simple Python app that generates creative ideas using Google's Gemini API.

## Features
- Prompts the user for a topic and generates 5 creative ideas using Gemini.
- Keeps your API key secure using a `.env` file.
- Easy to set up and run in a virtual environment.

## Setup Guide

### 1. Clone the repository
```
git clone https://github.com/YOUR_USERNAME/gemini-ideas.git
cd gemini-ideas
```

### 2. Create and activate a virtual environment (recommended)
On Windows (PowerShell):
```
python -m venv .venv
.\.venv\Scripts\Activate
```

### 3. Install requirements
```
pip install -r requirements.txt
```

### 4. Set up your environment variables
Create a `.env` file in the project folder with this content:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Run the app
```
python app.py
```

## Notes
- Never commit your `.env` file or API keys to version control.
- If you use a different API or add features, update `requirements.txt` and this README.

---

Enjoy generating creative ideas!
