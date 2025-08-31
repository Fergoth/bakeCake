from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phonenumber = models.CharField(
        "Номер телефона", null=False, blank=False, unique=True
    )
    name = models.CharField("Имя", max_length=255, blank=True, null=True)
    email = models.EmailField("Почта", max_length=255, blank=True, null=True)
    address = models.CharField("Адрес", max_length=255, blank=True, null=True)
    USERNAME_FIELD = "phonenumber"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        indexes = [
            models.Index(fields=["phonenumber"]),
        ]

    def __str__(self):
        return f"{self.name} {self.phonenumber}"
