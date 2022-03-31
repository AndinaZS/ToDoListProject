from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
