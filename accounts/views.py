from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Student, Admin
from .forms import StudentForm, AdminForm, DeactivateAdminForm, ReactivateAdminForm

User = get_user_model()

def student_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_student:
                login(request, user)
                return redirect('student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/student_login.html', {'form': form})

def admin_login_view(request):
    if request.method == 'POST':
        nuid = request.POST['nuid']
        try:
            admin = Admin.objects.get(NUID=nuid)
            if admin.user.is_admin:
                login(request, admin.user)
                return redirect('admin_profile')
        except Admin.DoesNotExist:
            pass  # error message here
    return render(request, 'accounts/admin_login.html')

def admin_profile_view(request):
    admin = request.user.admin_profile
    return render(request, 'accounts/admin_profile.html', {'admin': admin})

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

def admin_list_view(request):
    admins = Admin.objects.all()
    return render(request, 'accounts/admin_list.html', {'admins': admins})

def deactivate_admin_view(request):
    if request.method == 'POST':
        form = DeactivateAdminForm(request.POST)
        if form.is_valid():
            admin_id = form.cleaned_data['admin_id']
            admin = get_object_or_404(Admin, pk=admin_id)
            admin.is_active = False
            admin.deactivated_at = timezone.now()
            admin.save()
            return redirect('admin_list')
    else:
        form = DeactivateAdminForm()
    return render(request, 'accounts/deactivate_admin.html', {'form': form})

@login_required
def reactivate_admin_view(request):
    if request.method == 'POST':
        form = ReactivateAdminForm(request.POST)
        if form.is_valid():
            admin_id = form.cleaned_data['admin_id']
            admin = get_object_or_404(Admin, pk=admin_id)
            admin.is_active = True
            admin.deactivated_at = None
            admin.save()
            return redirect('admin_list')
    else:
        form = ReactivateAdminForm()
    return render(request, 'accounts/reactivate_admin.html', {'form': form})

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
