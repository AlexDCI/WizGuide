from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Translation
from .serializers import TranslationSerializer
import openai
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_client import get_response_from_openai
from .translate import translate_text_with_openai, save_translation_to_db  # Подключаем наши функции



load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


@csrf_exempt
def translate_text(request):
    print(f"Request body: {request.body}")  # Логируем тело запроса для диагностики

    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Разбираем JSON из тела запроса
            print(f"Parsed data: {data}")  # Логируем разобранные данные

            input_text = data.get('text')  # Извлекаем исходный текст
            target_language = data.get('language')  # Извлекаем целевой язык

            if not input_text or not target_language:
                return JsonResponse({"error": "Text or language not provided."}, status=400)
            
            # Получаем переведенный текст от OpenAI
            translated_text = get_response_from_openai(input_text, target_language)
            
            # Сохраняем перевод в базу данных
            translation = Translation(
                original_text=input_text,
                source_language="English",  # Предполагаем, что исходный язык всегда английский
                translated_text=translated_text,
                target_language=target_language
            )
            translation.save()  # Сохраняем в базе данных

            return JsonResponse({
                "original_text": input_text,
                "translated_text": translated_text,
                "source_language": "English",  # Можно динамически определять язык, если нужно
                "target_language": target_language
            })
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
# @csrf_exempt
# def translate_text(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         input_text = data.get("text")
#         target_language = data.get("language")

#         if not input_text or not target_language:
#             return JsonResponse({"error": "Text or language not provided."}, status=400)

#         try:
#             # Отправляем запрос к OpenAI через Chat API для перевода
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # Модель для работы с чатом
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": f"Translate the following text to {target_language}: {input_text}"}
#                 ]
#             )

#             # Получаем перевод из ответа
#             translation = response['choices'][0]['message']['content'].strip()

#             return JsonResponse({"translation": translation})

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

# @api_view(['POST'])
# def translate_text(request):
#     original_text = request.data.get('text')
#     source_language = request.data.get('source_language')
#     target_language = request.data.get('target_language')

#     if not original_text or not source_language or not target_language:
#         return Response({"error": "All fields (text, source_language, target_language) are required."}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         translated_text = get_translation(original_text, source_language, target_language)
#         return Response({"translated_text": translated_text}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# @api_view(['POST'])
# def save_translation(request):
#     serializer = TranslationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def test_api_view(request):
#     return Response({"message": "API is working"})

@csrf_exempt
def test_openai(request):
    print(f"Request body: {request.body}")  # Это поможет увидеть, что именно приходит на сервер
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Разбираем JSON из тела запроса
            print(f"Parsed data: {data}")  # Логируем разобранные данные
            user_message = data.get('user_message')
            
            if not user_message:
                return JsonResponse({"error": "No message provided."}, status=400)
            
            ai_response = get_response_from_openai(user_message)
            return JsonResponse({"ai_response": ai_response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)