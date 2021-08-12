from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('course/<str:pk>', views.course_detail, name='course_detail'),
    path('enroll/<str:pk>', views.enroll_course, name='enroll_course'),
    path('my_courses/', views.my_courses, name='my_courses'),
]
