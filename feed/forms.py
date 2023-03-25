from django import forms
from .models import Recipe


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        