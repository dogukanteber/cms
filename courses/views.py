from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserDetailForm, UserRegisterForm, UserInfo
from .models import Course

from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'courses/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'courses/register.html', { 'form': form })

def dashboard(request):
    courses = Course.objects.all()

    return render(request, 'courses/dashboard.html', { 'courses':courses })

def course_detail(request, pk):
    cd = Course.objects.get(id=pk)
    students = cd.students.all()

    return render(request, 'courses/course_detail.html', {'cd':cd, 'students':students })

def my_courses(request):
    user = User.objects.get(username=request.user)
    registered_courses = user.course_set.all()

    return render(request, 'courses/my_courses.html', { 'registered_courses': registered_courses })

def enroll(request):
    form = UserDetailForm()
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'courses/enroll.html', context)