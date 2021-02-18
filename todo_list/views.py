from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ListForm
from .models import List

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

def delete(req, item_id):
    item = get_object_or_404(List, pk=item_id)
    item.delete()
    messages.success(req, ('Item Deleted'))
    return redirect('home')

def mark_done(req, item_id):
    item = get_object_or_404(List, pk=item_id)
    item.is_completed = True
    item.save()
    messages.success(req, ('Item Updated'))
    return redirect('home')