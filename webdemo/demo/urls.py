from django.contrib import admin
from django.urls import path, include
from . import views, ajax_views

urlpatterns = [
    path('home/', views.home),
    path('index/', views.index),
    path('country/', views.country_info),
    path('employees/', views.list_employees),
    path('add/', views.add_employee),
    path('update/', views.update_salary),
    path('ajax/', ajax_views.ajax_demo),
    path('datetime/', ajax_views.send_datetime),
]