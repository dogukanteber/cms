from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserDetailForm, UserRegisterForm
from .models import Course

from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'courses/register.html', { 'form': form })

@login_required(login_url='login')
def dashboard(request):
    courses = Course.objects.all()

    return render(request, 'courses/dashboard.html', { 'courses':courses })

@login_required(login_url='login')
def course_detail(request, pk):
    cd = Course.objects.get(id=pk)
    students = cd.students.all()

    is_already_enrolled = False
    for student in students:
        if student == request.user:
            is_already_enrolled = True

    context = {
        'cd':cd,
        'students':students,
        'is_already_enrolled': is_already_enrolled,
    }

    return render(request, 'courses/course_detail.html', context)

@login_required(login_url='login')
def my_courses(request):
    user = User.objects.get(username=request.user)
    registered_courses = user.course_set.all()

    return render(request, 'courses/my_courses.html', { 'registered_courses': registered_courses })


@login_required(login_url='login')
def enroll_course(request, pk):
    cd = Course.objects.get(id=pk)

    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            cd.students.add(request.user.id)
            form.save()
            return redirect('dashboard')
    else:
        form = UserDetailForm()

    return render(request, 'courses/enroll_course.html', { 'form': form, 'cd':cd })