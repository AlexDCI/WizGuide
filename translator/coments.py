# from django.db import models
# from users.models import CustomUser  # импортируем модель CustomUser

# class Translation(models.Model):
#     original_text = models.TextField(verbose_name="Original Text")
#     source_language = models.CharField(max_length=50, verbose_name="Source Language")
#     translated_text = models.TextField(verbose_name="Translated Text")
#     target_language = models.CharField(max_length=50, verbose_name="Target Language")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
#     # Добавляем связь с пользователем
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='translations')

#     def __str__(self):
#         return f"{self.source_language} to {self.target_language}: {self.original_text[:30]}..


# from django.db import models

# class Translation(models.Model):
#     original_text = models.TextField(verbose_name="Original Text")
#     source_language = models.CharField(max_length=50, verbose_name="Source Language")
#     translated_text = models.TextField(verbose_name="Translated Text")
#     target_language = models.CharField(max_length=50, verbose_name="Target Language")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")  # добавим дату создания записи

#     def __str__(self):
#         return f"{self.source_language} to {self.target_language}: {self.original_text[:30]}..."


'''
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTY4OTkzMCwiaWF0IjoxNzMxNjAzNTMwLCJqdGkiOiI3YWIzNWQ0NWIxMDE0ZDM5OWZkM2UyOTMxNTMyMzlhMCIsInVzZXJfaWQiOjJ9.8SqTigG5YHL0DL8eW0y0C2fKrT6LHqjNOvILjJLgyuo",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNjAzODMwLCJpYXQiOjE3MzE2MDM1MzAsImp0aSI6ImUwNTU3YjI0MjE1YTQzMzU5MjM2ZmEwMjg1MWQ1ZDI0IiwidXNlcl9pZCI6Mn0.kOE5C0U2f-FW8eCZgPLc1dIb04xM2rGcm1WlbkoZqJg"
}
'''