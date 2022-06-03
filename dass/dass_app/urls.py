from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('form',views.form, name='form'),
    path('dassform',views.get_name,name="dassform"),
    path('submitform',views.submitform,name="submitform")
]