import logging
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

from DASH_pillars.forms import ScholarshipForm, HardshipForm, BasicNeedSupportForm
from .forms import StudentForm, AdminForm, CustomUserCreationForm, VisitReasonForm
from .models import StudentProfile, AdminProfile

logger = logging.getLogger(__name__)
User = get_user_model()


def student_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.user_type == 'student':
                login(request, user)
                return redirect('student_profile', NUID=user.NUID)
            else:
                form.add_error(None, "You are not authorized as a student.")
    else:
        form = AuthenticationForm()
    return render(request, 'student/student_login.html', {'form': form})


def admin_login_view(request):
    if request.method == 'POST':
        nuid = request.POST.get('nuid')
        password = request.POST.get('password')
        user = authenticate(request, username=nuid, password=password)
        if user is not None:
            if user.user_type == 'admin':
                login(request, user)
                return redirect('admin_profile')
            else:
                return render(request, 'admin/admin_login.html', {'error': 'You are not authorized as an admin.'})
        else:
            return render(request, 'admin/admin_login.html', {'error': 'Invalid NUID or password'})
    else:
        return render(request, 'admin/admin_login.html')


def register_admin(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        admin_form = AdminForm(request.POST)
        if user_form.is_valid() and admin_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'admin'
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
            return redirect('admin_list')
    else:
        user_form = CustomUserCreationForm()
        admin_form = AdminForm()
    return render(request, 'admin/register_admin.html', {'user_form': user_form, 'admin_form': admin_form})


@login_required(login_url='admin_login')
def admin_profile_view(request):
    try:
        admin_profile = request.user.adminprofile
    except AdminProfile.DoesNotExist:
        return redirect('admin_login')
    return render(request, 'admin/admin_profile.html', {'admin_profile': admin_profile})


def add_admin(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        admin_form = AdminForm(request.POST)
        if user_form.is_valid() and admin_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'admin'
            user.username = user.NUID  # Ensure the username is set to NUID
            user.save()
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
            return redirect('admin_list')
    else:
        user_form = CustomUserCreationForm()
        admin_form = AdminForm()
    return render(request, 'admin/add_admin.html', {'user_form': user_form, 'admin_form': admin_form})


def edit_admin(request, NUID):
    admin = get_object_or_404(AdminProfile, user_id=NUID)
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=admin.user)
        admin_form = AdminForm(request.POST, instance=admin)
        if user_form.is_valid() and admin_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'admin'
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            admin_form.save()
            return redirect('admin_list')
    else:
        user_form = CustomUserCreationForm(instance=admin.user)
        admin_form = AdminForm(instance=admin)
    return render(request, 'admin/edit_admin.html', {'user_form': user_form, 'admin_form': admin_form})


def admin_list_view(request):
    admins = AdminProfile.objects.all()
    return render(request, 'admin/admin_list.html', {'admins': admins})


def student_profile(request, NUID):
    student = get_object_or_404(StudentProfile, user_id=NUID)
    return render(request, 'student/student_profile.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        student_form = StudentForm(request.POST)
        scholarship_form = ScholarshipForm(request.POST)
        hardship_form = HardshipForm(request.POST)
        basic_needs_support_form = BasicNeedSupportForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'student'
            user.username = user.NUID  # Ensure the username is set to NUID
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('student_information')
    else:
        user_form = CustomUserCreationForm()
        student_form = StudentForm()
        scholarship_form = ScholarshipForm()
        hardship_form = HardshipForm()
        basic_needs_support_form = BasicNeedSupportForm()
    return render(request, 'student/add_student.html',
                  {'user_form': user_form, 'student_form': student_form, 'scholarship_form': scholarship_form,
                   'hardship_form': hardship_form, 'basic_needs_support_form': basic_needs_support_form})


def edit_student(request, NUID):
    student = get_object_or_404(StudentProfile, user_id=NUID)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_profile', NUID=student.user.NUID)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/edit_student.html', {'form': form})


def student_information(request):
    students = StudentProfile.objects.all()
    return render(request, 'student/student_information.html', {'students': students})

def visit_reason(request):
    if request.method == 'POST':
        form = VisitReasonForm(request.POST)
        if form.is_valid():
            # If valid print form
            print(form.cleaned_data)
    else:
        form = VisitReasonForm()

    return render(request, 'student/visit_reason.html', {'form': form})

    students = StudentProfile.objects.all().order_by('user__last_name', 'user__first_name')

    active_students = students.filter(user__is_active=True)
    inactive_students = students.filter(user__is_active=False)

    sorted_students = list(active_students) + list(inactive_students)

    return render(request, 'student/student_information.html', {'students': sorted_students})


