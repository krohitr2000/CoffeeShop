from django.shortcuts import render
from django.http import HttpResponse
from .models import coffee

def home(request):
    coffee = coffee.objects.all()
    return render(request,'home.hmtl',{'coffee':coffee})
    