from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    REGULAR_MEMBER = 1
    SERVICE_PROVIDER = 2
    ADMINISTRATOR = 3
    USER_TYPE_CHOICES = (
        (REGULAR_MEMBER, 'Regular Member'),
        (SERVICE_PROVIDER, 'Service Provider'),
        (ADMINISTRATOR, 'Administrator')
    )

    user = models.OneToOneField(User)
    user_type = models.IntegerField(
            choices=USER_TYPE_CHOICES,
            default=1)
    street = models.CharField(blank=False, max_length=100)
    country = models.CharField(blank=False, max_length=60)
    province = models.CharField(blank=False, max_length=50)
    city = models.CharField(blank=False, max_length=50)
    postal_code = models.CharField(blank=False, max_length=20)

    def location(self):
        address = [self.street, self.city, self.province, self.postal_code, self.country]
        return ', '.join(address)
