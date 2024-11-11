import openai
import os

# Установите ключ API
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(message):
    openai.api_key = "YOUR_SECRET_OPENAI_API_KEY"  # Ensure this is loaded from an environment variable in production
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}],
            temperature=0.7
        )
        # Extracting content from response
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"