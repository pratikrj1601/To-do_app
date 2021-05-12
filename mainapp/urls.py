from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo)
]