from django import forms

from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'is_completed']