from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'social_life', 'grade', 'dependence'
    )