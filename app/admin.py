from django.contrib import admin

# Register your models here.
from .models import DataReact,DataEncadreur

admin.site.register(DataReact)
admin.site.register(DataEncadreur)