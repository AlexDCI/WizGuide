from rest_framework import serializers
from .models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Translation
        fields = ['id', 'original_text', 'source_language', 'translated_text', 'target_language', 'created_at', 'user']

    def get_user(self, obj):
        # Локально импортируем CustomUserSerializer только внутри метода
        from users.serializers import CustomUserSerializer
        
        # Сериализуем пользователя, связанного с переводом
        user_serializer = CustomUserSerializer(obj.user)
        return user_serializer.data

# from rest_framework import serializers
# from .models import Translation

# class TranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Translation
#         fields = ['id', 'original_text', 'source_language', 'translated_text', 'target_language']


