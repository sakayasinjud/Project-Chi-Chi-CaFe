from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.menu_list),
    path('add/', views.add_menu),
    path('edit/<int:id>/', views.edit_menu),
    path('delete/<int:id>/', views.delete_menu),
    path('about/', views.about),
]