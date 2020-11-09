from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User, Teacher, Student
from django.db import transaction


class TeacherRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2']

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_Teacher = True
        user.first_name = self.cleaned_data.get('first_name')
        user.first_name = self.cleaned_data.get('last_name')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher = user.is_Teacher
        teacher.phone_number = self.cleaned_data.get('phone_number')
        teacher.save()
        return teacher


class StudentRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    registration_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2']

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.first_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student = user.is_Student
        student.registration_number = self.cleaned_data.get(
            'registration_number')
        student.save()
        return student


class UpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
