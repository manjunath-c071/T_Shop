from django.shortcuts import render, redirect
from .models import Product
from . import forms

from django.views.generic import(
    CreateView,
    ListView, DetailView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy, reverse


# Create your views here.
class ProductList(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'


from django.views.generic.edit import FormMixin

class ProductDetailView(FormMixin, DetailView):
    template_name = 'products/product_details.html'
    model = Product
    context_object_name = 'product'
    form_class = forms.ProductImageForm

    def get_success_url(self):
        return reverse('prod_details', kwargs = {'pk': self.this_product.pk})

    def post(self, request, *args, **kwargs):
        self.this_product = self.get_object()
        submitted_image_form = self.get_form()


        if submitted_image_form.is_valid():
            product_image = submitted_image_form.save(commit = False)
            product_image.product = self.this_product
            product_image.save()
            return redirect(self.get_success_url())

class AddProduct(CreateView):
    model = Product
    template_name = 'products/add_product.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/edit_product.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/del_product.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product' 


from .models import ProductImage
class UpdateProductImage(UpdateView):
    model = ProductImage
    template_name = 'products/edit_product_image.html'
    form_class = forms.ProductImageForm
    success_url = reverse_lazy('product_list')
    
class DeleteProductImage(DeleteView):
    model = ProductImage
    template_name = 'products/del_product_image.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product_image' 