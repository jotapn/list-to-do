from django.contrib import admin
from .models import Usuario, Card

models = [Usuario, Card]
admin.site.register(models)
