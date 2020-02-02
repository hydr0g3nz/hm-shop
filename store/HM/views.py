from django.shortcuts import render
from django.http import HttpResponse
from .models import AllProduct

def Home(req):
    return render(req,'HM/home.html')

def about(req):
    return render(req,'HM/about.html')

def Shop(req):
    allproduct = AllProduct.objects.all()
    context = {'allproduct':allproduct}
    return render(req,'HM/shop.html',context)

# Create your views here.
