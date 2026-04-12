from django import forms
from .models import Product, ProductImage, Brand

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['title', 'desc', 'category', 'brand', 'thumbnail', 'price', 'stock']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),  # ✅ NEW
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_brand(self):
        brand = self.cleaned_data.get('brand')
        if not brand:
            raise forms.ValidationError("Brand is required")
        return brand


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage 
        fields = ['image', 'caption']

        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
        }