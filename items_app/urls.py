from django.urls import path, include
from . import views

urlpatterns = [
    path('laptops/', views.LaptopsView, name='LaptopsView'),
    path('laptop/<int:pk>/', views.GetLaptop_View, name='GetLaptop_View'),
]
