from django.db import models
from django.utils import timezone
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


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField(null=False, blank=False)
    valid_to = models.DateTimeField(null=False, blank=False)

    def is_valid(self):
        now = timezone.now()
        if self.valid_from is None or self.valid_to is None:
            return False
        return self.valid_from <= now <= self.valid_to

    def __str__(self):
        return self.code
