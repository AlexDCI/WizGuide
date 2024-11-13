import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



def get_response_from_openai(user_message, target_language):
    try:
        # Используем API v1/chat/completions с моделью gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Убедитесь, что выбрали правильную модель
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Translate the following text to {target_language}: {user_message}"}
            ]
        )

        # Извлекаем переведенный текст
        return response['choices'][0]['message']['content'].strip()
    except openai.error.OpenAIError as e:
        raise Exception(f"OpenAI error: {str(e)}")

