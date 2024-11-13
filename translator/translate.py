# translate.py (или в другом соответствующем файле)
import openai
from .models import Translation
from .openai_client import get_response_from_openai
from django.http import JsonResponse
from dotenv import load_dotenv
import os
import json


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_and_validate_data(request):
    try:
        data = json.loads(request.body)
        input_text = data.get('text')
        target_language = data.get('language')

        if not input_text or not target_language:
            return None, JsonResponse({"error": "Text or language not provided."}, status=400)

        return (input_text, target_language), None
    except json.JSONDecodeError:
        return None, JsonResponse({"error": "Invalid JSON format."}, status=400)


def translate_text_via_openai(input_text, target_language):
    try:
        translated_text = get_response_from_openai(input_text, target_language)
        return translated_text, None
    except openai.error.OpenAIError as e:
        return None, JsonResponse({"error": f"OpenAI error: {str(e)}"}, status=500)



def save_translation_to_db(input_text, translated_text, target_language):
    translation = Translation(
        original_text=input_text,
        source_language="English",  # Это можно сделать динамическим при необходимости
        translated_text=translated_text,
        target_language=target_language
    )
    translation.save()