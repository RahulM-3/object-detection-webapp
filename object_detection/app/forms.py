from django import forms
from app.models import uploadimage

class imageform(forms.ModelForm):
    class Meta:
        model = uploadimage
        fields = {'image'}