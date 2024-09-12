from django import forms

class LinkForm(forms.Form):
    name = forms.CharField(max_length=50)
    url = forms.URLField(max_length=500)
    slug = forms.SlugField(required=False)