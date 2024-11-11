from django.db import models

class Translation(models.Model):
    original_text = models.TextField(verbose_name="Original Text")
    source_language = models.CharField(max_length=50, verbose_name="Source Language")
    translated_text = models.TextField(verbose_name="Translated Text")
    target_language = models.CharField(max_length=50, verbose_name="Target Language")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")  # добавим дату создания записи

    def __str__(self):
        return f"{self.source_language} to {self.target_language}: {self.original_text[:30]}..."