from django.contrib import admin

from server import models


@admin.register
class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Person
