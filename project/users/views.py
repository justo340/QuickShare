from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
                    TeacherRegisterForm,
                    ProfileUpdateForm,
                    UpdateForm,
                    StudentRegisterForm
                    )
from .models import User


def register(request):
    return render(request, 'users/register.html')


def registerTeacher(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = User
            user.is_Teacher = True
            form.save()
            messages.success = (
                request,
                f'Your account has been created! You are now able to Login')
            user = User
            user.is_Teacher = True
            return redirect('login')
    else:
        form = TeacherRegisterForm()
    return render(request, 'users/teacher_register.html', {'form': form})


def registerStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = User
            user.is_Student = True
            form.save()
            messages.success = (
                request,
                f'Your account has been created! You are now able to Login')
            user = User
            user.is_Student = True
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'users/student_register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success = (request, f' Your account has been updated! ')
            return redirect('profile')

    else:
        u_form = UpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
