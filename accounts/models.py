from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user_city = ChainedForeignKey(
        City,
        chained_field='user_country',
        chained_model_field='country',
        null=True,
        blank=True
    )
    birthday = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)





