# translator/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
import openai
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .translate import extract_and_validate_data, translate_text_via_openai, save_translation_to_db  # Подключаем наши функции
from .openai_client import get_response_from_openai
from rest_framework import generics
from .models import Translation
from .serializers import TranslationSerializer
from rest_framework.permissions import IsAuthenticated


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



from rest_framework.decorators import permission_classes

@csrf_exempt
@permission_classes([IsAuthenticated])  # Добавляем проверку на аутентификацию
def translate_text(request):
    if request.method == 'POST':
        # Проверка на аутентификацию пользователя (по сути, это уже делается через permission_classes)
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        
        # Извлечение и валидация данных
        data, error_response = extract_and_validate_data(request)
        if error_response:
            return error_response

        input_text, target_language = data

        # Перевод текста через OpenAI
        translated_text, error_response = translate_text_via_openai(input_text, target_language)
        if error_response:
            return error_response

        # Получаем пользователя из запроса
        user = request.user

        # Сохраняем перевод в базу данных, привязывая его к пользователю
        save_translation_to_db(input_text, translated_text, target_language, user)

        # Ответ с результатом
        return JsonResponse({
            "original_text": input_text,
            "translated_text": translated_text,
            "source_language": "English",
            "target_language": target_language
        })


class TranslationListView(generics.ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

class TranslationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    


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