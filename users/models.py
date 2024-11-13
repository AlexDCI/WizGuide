from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('premium', 'Premium User'),
        ('admin', 'Administrator'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')
    trial_expiry_date = models.DateField(null=True, blank=True)

    # Добавление related_name для поля groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное имя для обратной связи с группами
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Уникальное имя для обратной связи с правами
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
