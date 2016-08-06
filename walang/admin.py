from django.contrib import admin

from walang import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'user', 'user_type', 'email')

@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'worker', 'requester', 'status', 'payable')

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('service', 'worker', 'rate')
