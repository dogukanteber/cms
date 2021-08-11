from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('course/<str:pk>', views.course_detail, name='course_detail'),
    path('enroll/', views.enroll, name='enroll'),
    path('my_courses/', views.my_courses, name='my_courses'),
]
