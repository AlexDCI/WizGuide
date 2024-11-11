from django.urls import path
from .views import test_openai, translate_text
# test_api_view, save_translation, translate_text, test_openai

urlpatterns = [
    # path('test/', test_api_view, name='test-api'),
    # path('save-translation/', save_translation, name='save-translation'),
    # path('translate/', translate_text, name='translate-text'),
    path('test-openai/', test_openai, name='test_openai'),
    path('api/translate/', translate_text, name='translate_text'),
]