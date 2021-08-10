from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('course/<str:pk>', views.course_detail, name='course_detail'),
]
