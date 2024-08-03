from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Admin
from .forms import StudentForm, AdminForm, RemoveAdminForm

def student_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_student:
                login(request, user)
                return redirect('student_dashboard')  # Change to your student dashboard URL
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/student_login.html', {'form': form})

def admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_admin:
                login(request, user)
                return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/admin_login.html', {'form': form})

def admin_profile_view(request):
    student = Student.objects.first()
    return render(request, 'accounts/admin_profile.html', {'student': student})


def add_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    else:
        form = AdminForm()
    return render(request, 'accounts/add_admin.html', {'form': form})

def edit_admin(request, id):
    admin = get_object_or_404(Admin, id=id)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    else:
        form = AdminForm(instance=admin)
    return render(request, 'accounts/edit_admin.html', {'form': form})

def remove_admin(request):
    if request.method == 'POST':
        form = RemoveAdminForm(request.POST)
        if form.is_valid():
            nuid = form.cleaned_data['nuid']
            confirm_nuid = form.cleaned_data['confirm_nuid']
            if nuid == confirm_nuid:
                admin = get_object_or_404(Admin, nuid=nuid)
                admin.delete()
                return redirect('admin_profile')
    else:
        form = RemoveAdminForm()
    return render(request, 'accounts/remove_admin.html', {'form': form})


def student_profile(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'accounts/student_profile.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_information')
    else:
        form = StudentForm()
    return render(request, 'accounts/add_student.html', {'form': form})

def remove_student(request):
    if request.method == 'POST':
        NUID = request.POST.get('nuid')
        student = get_object_or_404(Student, NUID=NUID)
        student.delete()
        return redirect('student_information')
    return render(request, 'accounts/remove_student.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_profile', id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'accounts/edit_student.html', {'form': form})

def student_information(request):
    students = Student.objects.all()
    return render(request, 'accounts/student_information.html', {'students': students})

