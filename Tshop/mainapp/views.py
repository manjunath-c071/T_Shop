from django.shortcuts import render
from .models import CarouselImage

# Views.py handles request-response
# It also handles the DML and DQL operations required for the same.

from products.models import Product, Brand
from accessories.models import Accessory

# Create your views here.

def homeView(request):
    template = 'mainapp/home.html'
    context = {
        # This will be an array of all active carousel image objects mapped from DB
        'carousel_images' : CarouselImage.objects.filter(is_active = True),
        'products' : Product.objects.all(),
        'brands': Brand.objects.filter(product__isnull=False).distinct(),  # Get brands that have at least one product
        'accessories': Accessory.objects.all()
     
        }
    return render(
        request = request,
        template_name= template,
        context= context
    )

def aboutView(request):
    template = 'mainapp/about.html'
    return render(
        request = request,
        template_name= template,
        context={}
    )

def contactView(request):
    template = 'mainapp/contact.html'

    return render(
        request = request,
        template_name= template,
        context={}
    )


# Class based generic views
from django.views.generic import (
    CreateView,
    ListView, DetailView,
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy

class CarouselImageList(ListView):
    template_name = 'mainapp/carousel/carousel_list.html'
    model = CarouselImage
    context_object_name = 'carousel_images'    

class AddCarouselImage(CreateView):
    model = CarouselImage
    template_name = 'mainapp/carousel/add_carousel.html'
    fields = '__all__'
    success_url = reverse_lazy('carousel_list')
    
class UpdateCarouselImage(UpdateView):
    model = CarouselImage
    template_name = 'mainapp/carousel/edit_carousel.html'
    fields = '__all__'
    success_url = reverse_lazy('carousel_list')
    
class DeleteCarouselImage(DeleteView):
    model = CarouselImage
    template_name = 'mainapp/carousel/del_carousel.html'
    success_url = reverse_lazy('carousel_list')
    context_object_name = 'carousel_image' 