from django.shortcuts import render
from .models import CarouselImage

# Create your views here.
def homeView(request):
    template = 'mainapp/home.html'
    context ={
        # Get all active carousel images that have an uploaded file
        'carousel_images': CarouselImage.objects.filter(is_active=True).exclude(file='').exclude(file__isnull=True)
    }

    return render(
        request = request,
        template_name = template,
        context= context
    )



def aboutView(request):
    template = 'mainapp/about.html'


    return render(
        request = request,
        template_name = template,
        context={}
    )

def contactView(request):
    template = 'mainapp/contact.html'


    return render(
        request = request,
        template_name = template,
        context={}
    )
#Class based generic views 
from django.views.generic import (
    CreateView,
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)
class CarouselImageList(ListView):
    template_name  = 'mainapp/carousel/carousel_list.html'
    model = CarouselImage
    context_object_name = 'carousel_images'       


class AddCarouselImage(CreateView):
    model = CarouselImage
    template_name = 'mainapp/carousel/add_carousel.html'
    fields = '__all__'
    success_url = '/'
    
class UpdateCarouselImage(UpdateView):
    model = CarouselImage
    template_name = 'mainapp/carousel/edit_carousel.html'
    fields = '__all__'
    success_url = '/'
    

class DeleteCarouselImage(DeleteView):
    model = CarouselImage
    template_name = 'mainapp/carousel/del_carousel.html'
    success_url = '/'