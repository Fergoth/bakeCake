from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phonenumber = models.CharField(
        "Номер телефона", null=False, blank=False, unique=True
    )
    avatar = models.ImageField("картинка", upload_to="avatars/", null=True, blank=True)
    name = models.CharField("Имя", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        indexes = [
            models.Index(fields=["phonenumber"]),
        ]

    def __str__(self):
        return f"{self.name} {self.phonenumber}"
