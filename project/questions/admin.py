from django.contrib import admin
from .models import *
# Register your models here.

class Question_Inline(admin.TabularInline):
    model = Question
    extra = 0

class Decision_Inline(admin.TabularInline):
    model = Decision
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'index', 'pub_date'
    )
    inlines = [Decision_Inline]

@admin.register(Endings)
class EndingsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'social_life', 'grade', 'dependence'
    )