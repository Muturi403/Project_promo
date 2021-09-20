from django.contrib import admin
# Register your models here.
from . import models

admin.site.register(models.Projects)
admin.site.register(models.Profile)
admin.site.register(models.Rate)
