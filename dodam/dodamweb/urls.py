from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shelf/', views.shelf, name='shelf'),
    path('shelf1/', views.shelf1, name='shelf1'),
   
    path('spec/', views.spec, name='spec'),
]