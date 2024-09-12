from django import forms
from .models import Links
class LinkForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['name', 'url', 'slug']
        labels = {
            'name': 'Link Name',
        }

        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'Enter URL here'})
        }