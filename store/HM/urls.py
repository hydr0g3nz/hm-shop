from django.urls import path, include 
from .views import Home,about,Shop
urlpatterns = [
    path('', Home, name='home-page'),
    path('about/',about, name='about-page'),
    path('shop/',Shop,name='shop-page')
   
]
