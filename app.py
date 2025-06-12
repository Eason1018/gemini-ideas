import os # We'll use this later for a better way to handle the key
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=API_KEY)

# Add this code below the configuration
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Add this code below setting up the model
print("🚀 Welcome to the Idea Generator! 🚀")
print("------------------------------------")
print("Enter a topic, and I'll give you 5 creative ideas.")
print("Type 'quit' or 'exit' to end the program.\n")

while True:
    # Get user input
    user_topic = input("Enter a topic: ")

    # Check if the user wants to quit
    if user_topic.lower() in ['quit', 'exit']:
        print("Goodbye! 👋")
        break
    
    # This is our instruction to the model
    prompt = f"""
    You are a world-class creative idea generation machine.
    Your goal is to generate 5 innovative and distinct ideas based on a given topic.
    Present the ideas as a numbered list. Be concise but inspiring.

    TOPIC: "{user_topic}"
    """

    # Call the API
    response = model.generate_content(prompt)

    # Print the result
    print("\n💡 Here are your ideas: \n")
    print(response.text)
    print("\n------------------------------------\n")