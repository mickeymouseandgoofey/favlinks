from django.urls import path
from . import views

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('add/', views.add_link, name='add_link'),
]
