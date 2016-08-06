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
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    SINGLE = 1
    MARRIED = 2
    DIVORCED = 3
    WIDOWED = 4
    MARITAL_STATUS_CHOICES = (
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widowed')
    )

    user = models.OneToOneField(User)
    user_type = models.SmallIntegerField(choices=USER_TYPE_CHOICES,
                                         default=REGULAR_MEMBER)
    city = models.CharField(blank=False, max_length=50)
    contact_number = models.CharField(max_length=12, blank=False)
    country = models.CharField(blank=False, max_length=60)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=MALE)
    member_since = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='pictures')
    postal_code = models.CharField(blank=False, max_length=20)
    province = models.CharField(blank=False, max_length=50)
    street = models.CharField(blank=False, max_length=100)
    marital_status = models.SmallIntegerField(choices=MARITAL_STATUS_CHOICES,
                                              default=SINGLE)
    bio = models.TextField(max_length=300)
    services = models.ManyToManyField('Service', through='Rate', related_name='offerers')

    def address(self):
        address = [self.street, self.city, self.province, self.postal_code, self.country]
        return ', '.join(address)

    def __unicode__(self):
        return self.user.get_full_name()


class Request(models.Model):
    DONE = 1
    PENDING = 2
    ACCEPTED = 3
    STATUS_CHOICES = (
        (DONE, 'Done'),
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted')
    )
    rate = models.ForeignKey('Rate', related_name='requests')
    requester = models.ForeignKey('Person', related_name='request')
    date_requested = models.DateField(auto_now_add=True)
    date_completed = models.DateField(blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    feedback = models.TextField(blank=True)
    positive_feedback = models.NullBooleanField(blank=True, null=True)
    payable = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    @property
    def service(self):
        return self.rate.service

    @property
    def worker(self):
        return self.rate.worker


class Rate(models.Model):
    service = models.ForeignKey('Service', related_name='rates')
    worker = models.ForeignKey('Person', related_name='rates')
    rate = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __unicode__(self):
        return str(self.rate)


class Service(models.Model):
    name = models.CharField(blank=False, max_length=30)

    def __unicode__(self):
        return self.name
