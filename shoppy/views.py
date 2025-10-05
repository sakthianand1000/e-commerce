import json
from django.shortcuts import render
from .models import Catagory, Products
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages

def home(request):
    return render(request,"shoppy_prods/index.html")

def form(request):
    return render(request,"shoppy_prods/form.html")

def collection(request):
    return render(request,"shoppy_prods/collection.html")

def collectionview(request):
    return render(request,"shoppy_prods/products/product_index.html")

def fav_page(request):
    return render(request,"shoppy_prods/fav_page.html")

def login_form(request):
    return render(request,"shoppy_prods/login_form.html")

def register(request):
    return render(request,"shoppy_prods/register.html")

def cart(request):
    return render(request,"shoppy_prods/cart.html")

