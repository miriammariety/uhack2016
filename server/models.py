from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    REGULAR_MEMBER = 1
    SERVICE_PROVIDER = 2
    ADMINISTRATOR = 3
    MALE = 1
    FEMALE = 2
    USER_TYPE_CHOICES = (
        (REGULAR_MEMBER, 'Regular Member'),
        (SERVICE_PROVIDER, 'Service Provider'),
        (ADMINISTRATOR, 'Administrator')
    )
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    user = models.OneToOneField(User)
    user_type = models.IntegerField(
            choices=USER_TYPE_CHOICES,
            default=REGULAR_MEMBER)
    city = models.CharField(blank=False, max_length=50)
    contact_number = models.CharField(max_length=12, blank=True)
    country = models.CharField(blank=False, max_length=60)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=MALE)
    member_since = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='pictures')
    postal_code = models.CharField(blank=False, max_length=20)
    province = models.CharField(blank=False, max_length=50)
    street = models.CharField(blank=False, max_length=100)

    def address(self):
        address = [self.street, self.city, self.province, self.postal_code, self.country]
        return ', '.join(address)


class Service(model.Model):
    name = models.CharField(blank=False, max_length=30)
    workers = models.ManyToManyField(related_name='services')
