from django import forms
from .models import Character

class Character_create_form(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name']

class Character_update_form(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['social_life', 'grade', 'dependence']

    
