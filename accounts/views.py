from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import StudentForm, AdminForm, DeactivateAdminForm, ReactivateAdminForm, CustomUserCreationForm
from .models import Student, Admin

import logging

logger = logging.getLogger(__name__)

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
    return render(request, 'student/student_login.html', {'form': form})


def admin_login_view(request):
    if request.method == 'POST':
        nuid = request.POST.get('nuid')
        logger.warning(f"Received NUID: {nuid}")
        if not nuid:
            return render(request, 'admin/admin_login.html', {'error': 'NUID is required'})

        try:
            admin = Admin.objects.get(NUID=nuid)
            user = admin.user
            logger.warning(f"Admin found: {admin}, User: {user}")
            if user and user.is_admin:
                login(request, user)
                next_url = request.GET.get('next', '/accounts/admin_profile')
                return HttpResponseRedirect(next_url)
        except Admin.DoesNotExist:
            logger.debug("Admin does not exist")
            return render(request, 'admin/admin_login.html', {'error': 'Invalid NUID or not an admin'})

    return render(request, 'admin/admin_login.html')

@login_required(login_url='admin_login')
def admin_profile_view(request):
    try:
        admin = request.user.admin_profile
    except Admin.DoesNotExist:
        # Handle the case where the authenticated user does not have an admin profile
        return redirect('admin_login')  # or another appropriate view

    return render(request, 'admin/admin_profile.html', {'admin': admin})


def add_admin(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        admin_form = AdminForm(request.POST)
        if user_form.is_valid() and admin_form.is_valid():
            user = user_form.save(commit=False)
            user.is_admin = True
            user.set_unusable_password()  # Set the password to be unusable for now
            user.save()

            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()

            return redirect('admin_profile')
    else:
        user_form = CustomUserCreationForm()
        admin_form = AdminForm()

    return render(request, 'admin/add_admin.html', {'user_form': user_form, 'admin_form': admin_form})


def edit_admin(request, id):
    admin = get_object_or_404(Admin, id=id)
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        admin_form = AdminForm(request.POST, instance=admin)
        if user_form.is_valid() and admin_form.is_valid():
            user = user_form.save(commit=False)
            user.is_admin = True
            user.set_unusable_password()  # Set the password to be unusable for now
            user.save()

            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
    else:
        user_form = CustomUserCreationForm()
        admin_form = AdminForm(instance=admin)
    return render(request, 'admin/edit_admin.html', {'user_form': user_form, 'admin_form': admin_form})


def admin_list_view(request):
    admins = Admin.objects.all()
    return render(request, 'admin/admin_list.html', {'admins': admins})


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
    return render(request, 'admin/deactivate_admin.html', {'form': form})


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
    return render(request, 'admin/reactivate_admin.html', {'form': form})


def student_profile(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student/student_profile.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_information')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})


def remove_student(request):
    if request.method == 'POST':
        NUID = request.POST.get('nuid')
        student = get_object_or_404(Student, NUID=NUID)
        student.delete()
        return redirect('student_information')
    return render(request, 'student/remove_student.html')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_profile', id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/edit_student.html', {'form': form})


def student_information(request):
    students = Student.objects.all()
    return render(request, 'student/student_information.html', {'students': students})
