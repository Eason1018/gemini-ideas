# list_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Securely get the API key from the environment
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=API_KEY)

print("Fetching available models...\n")

try:
    for m in genai.list_models():
        # Check if the model supports the 'generateContent' method
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
    print("\n✅ Test successful! If you see 'models/gemini-1.0-pro' above, your setup is correct.")

except Exception as e:
    print(f"\n❌ Test FAILED.")
    print(f"An error occurred: {e}")
    print("\nThis means the issue is still with your API key or Google Cloud Project permissions.")