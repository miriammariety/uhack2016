from django.contrib import admin

from server import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
