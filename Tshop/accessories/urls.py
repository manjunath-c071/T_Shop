from django.urls import path
from . import views

urlpatterns = [
    path('', views.accessory_list, name='accessory_list'),
    path('<int:pk>/', views.accessory_detail, name='accessory_detail'),
    path('add/', views.accessory_add, name='accessory_add'),
    path('<int:pk>/edit/', views.accessory_edit, name='accessory_edit'),
    path('<int:pk>/delete/', views.accessory_delete, name='accessory_delete'),
]