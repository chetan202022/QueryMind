import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

print("Welcome to QueryMind! Type 'exit' to quit.")

while True:
    user_input = input("YourMind: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ],
        "temperature": 0,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        bot_response = response.json()["choices"][0]["message"]["content"].strip()
        print(f"QueryMind: {bot_response}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)