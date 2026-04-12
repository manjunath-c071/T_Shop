from django import forms
from .models import Accessory

class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'category', 'desc', 'thumbnail', 'price', 'stock']