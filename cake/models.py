from django.db import models
from custom_user.models import User


# Create your models here.
class CakeLevel(models.Model):
    name = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.name} {self.price}Р"


class CakeForm(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.name} {self.price}Р"


class CakeTopping(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.name} {self.price}Р"


class CakeBerries(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.name} {self.price}Р"


class CakeDecor(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.name} {self.price}Р"


class CurentPhrasePrice(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f" {self.price}Р"


class CakeOrder(models.Model):
    level = models.ForeignKey(
        CakeLevel, on_delete=models.CASCADE, null=False, blank=False
    )
    form = models.ForeignKey(
        CakeForm, on_delete=models.CASCADE, null=False, blank=False
    )
    topping = models.ForeignKey(
        CakeTopping, on_delete=models.CASCADE, null=False, blank=False
    )
    berries = models.ForeignKey(
        CakeBerries, on_delete=models.CASCADE, null=True, blank=True
    )
    decor = models.ForeignKey(
        CakeDecor, on_delete=models.CASCADE, null=True, blank=True
    )
    phrase_on_cake = models.CharField(max_length=255, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField()
    courier_comment = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
