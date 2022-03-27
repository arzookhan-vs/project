from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
  path('', views.index, name='demo'),
  path('submit_form/', views.submit_form, name="submit_form"),
]
