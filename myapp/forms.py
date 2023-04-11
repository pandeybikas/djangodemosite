from django import forms
from .models import Product
from django.forms.widgets import FileInput
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'desc', 'images']
        widgets = {
            'images' : FileInput
        }