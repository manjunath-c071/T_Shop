from django.shortcuts import render
from .models import CarouselImage

# Create your views here.
def homeView(request):
    template = 'mainapp/home.html'
    context ={
        # Get all active carousel images from the database and pass them to the template
        'carousel_images': CarouselImage.objects.filter(is_active=True)
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