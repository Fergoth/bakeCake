from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    phonenumber = models.CharField(
        "Номер телефона", null=False, blank=False, unique=True
    )
    name = models.CharField("Имя", max_length=255, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        indexes = [
            models.Index(fields=["phonenumber"]),
        ]

    def save(self, *args, **kwargs):
        self.username = self.phonenumber
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.phonenumber}"
