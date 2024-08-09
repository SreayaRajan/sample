from django import forms
from .models import imagegallary
class imageForm(forms.ModelForm):
    class Meta:
        model=imagegallary
        fields=('caption','image')