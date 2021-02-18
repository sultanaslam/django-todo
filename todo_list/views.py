from django.http import request
from django.shortcuts import render
from django.contrib import messages

from .models import List
from .forms import ListForm
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item Added'))
            return home_response(request)
        else:
            return home_response(request)
    else:
        return home_response(request)

def home_response(request):
    items = List.objects.all()
    return render(request, 'home.html',{'items': items})