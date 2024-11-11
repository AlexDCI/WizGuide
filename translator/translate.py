# translate.py (или в другом соответствующем файле)
import openai
from .models import Translation

def translate_text_with_openai(input_text, target_language):
    try:
        # Отправляем запрос в OpenAI для перевода
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Используем модель GPT-3.5 или другую
            prompt=f"Translate the following text to {target_language}: {input_text}",
            max_tokens=1000
        )
        # Извлекаем переведенный текст
        translated_text = response.choices[0].text.strip()
        return translated_text
    except openai.error.OpenAIError as e:
        raise Exception(f"OpenAI error: {str(e)}")

def save_translation_to_db(original_text, source_language, translated_text, target_language):
    # Сохраняем перевод в базу данных
    translation = Translation(
        original_text=original_text,
        source_language=source_language,
        translated_text=translated_text,
        target_language=target_language
    )
    translation.save()
