from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .models import Course

@login_required
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

    return render(request, 'courses/dashboard.html', { 'courses': courses })

def course_detail(request, pk):
    cd = Course.objects.get(id=pk)

    return render(request, 'courses/course_detail.html', {'cd':cd })