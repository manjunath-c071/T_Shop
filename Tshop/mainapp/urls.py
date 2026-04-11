from django.urls import path 
from .views import (
    homeView, 
    aboutView,
    contactView
)

from . import views

urlpatterns = [
    path('', homeView, name = 'home_page'),
    path('about/', aboutView, name = 'about_page'),
    path('contact/', contactView, name = 'contact_page'),

    path('carousels/', views.CarouselImageList.as_view(), name = 'carousel_list'),
    path('carousels/add/', views.AddCarouselImage.as_view(), name = 'add_carousel'),
    path('carousels/edit/<int:pk>/', views.UpdateCarouselImage.as_view(), name = 'edit_carousel'),
    path('carousels/del/<int:pk>', views.DeleteCarouselImage.as_view(), name='del_carousel')

]