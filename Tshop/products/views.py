from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Product, ProductImage, Brand
from . import forms



class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff



class ProductList(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.filter(product__isnull=False).distinct()
        return context


class ProductDetailView(FormMixin, DetailView):
    template_name = 'products/product_details.html'
    model = Product
    context_object_name = 'product'
    form_class = forms.ProductImageForm

    def get_success_url(self):
        return reverse('prod_details', kwargs={'pk': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = self.get_form()

        if form.is_valid():
            img = form.save(commit=False)
            img.product = product
            img.save()
            return redirect(self.get_success_url())



class AddProduct(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Product
    template_name = 'products/add_product.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class UpdateProduct(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/edit_product.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class DeleteProduct(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/del_product.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'


class UpdateProductImage(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = ProductImage
    template_name = 'products/edit_product_image.html'
    form_class = forms.ProductImageForm
    success_url = reverse_lazy('product_list')


class DeleteProductImage(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = ProductImage
    template_name = 'products/del_product_image.html'
    success_url = reverse_lazy('product_list')