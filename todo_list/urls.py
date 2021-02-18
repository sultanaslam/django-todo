from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('done/<item_id>', views.mark_done, name='mark_done'),
    path('edit/<item_id>', views.update, name='update'),
]
