from django.urls import path
from django.urls import path
from .views import test_api_view, save_translation

urlpatterns = [
    path('test/', test_api_view, name='test-api'),
    path('save-translation/', save_translation, name='save-translation'),
]