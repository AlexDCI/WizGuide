from django.urls import path
from .views import test_openai, translate_text
from .views import TranslationListView, TranslationDetailView

urlpatterns = [

    path('test-openai/', test_openai, name='test_openai'),
    path('api/translate/', translate_text, name='translate_text'),
    path('translations/', TranslationListView.as_view(), name='translation-list'),
    path('translations/<int:pk>/', TranslationDetailView.as_view(), name='translation-detail'),
]