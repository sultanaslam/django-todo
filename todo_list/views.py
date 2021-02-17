from django.shortcuts import render

from .models import List

def home(request):
    items = List.objects.all()
    return render(request, 'home.html',{'items': items})