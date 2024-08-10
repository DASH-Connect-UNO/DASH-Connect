import logging
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

from DASH_pillars.forms import ScholarshipForm, HardshipForm, BasicNeedSupportForm
from .forms import StudentForm, AdminForm, CustomUserCreationForm, VisitReasonForm
from .models import StudentProfile, AdminProfile

logger = logging.getLogger(__name__)
User = get_user_model()


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
    admins = AdminProfile.objects.order_by('-user__is_active', 'user__first_name')
    return render(request, 'admin/admin_list.html', {'admins': admins})


def deactivate_admin(request, NUID):
    if request.method == "POST":
        admin = get_object_or_404(User, NUID=NUID)
        admin.is_active = False
        admin.save()
        return redirect('admin_list')


def reactivate_admin(request, NUID):
    if request.method == "POST":
        admin = get_object_or_404(User, NUID=NUID)
        admin.is_active = True
        admin.save()
        return redirect('admin_list')


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


def student_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.user_type == 'student':
                login(request, user)
                return redirect('visit_reason')  # Redirect to visit_reason page
            else:
                form.add_error(None, "You are not authorized as a student.")
    else:
        form = AuthenticationForm()
    return render(request, 'student/student_login.html', {'form': form})


def edit_student(request, NUID):
    student = get_object_or_404(StudentProfile, user_id=NUID)
    user = student.user

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=user)
        student_form = StudentForm(request.POST, instance=student)

        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            return redirect('student_profile', NUID=student.user.NUID)
    else:
        user_form = CustomUserCreationForm(instance=user)
        student_form = StudentForm(instance=student)

    return render(request, 'student/edit_student.html', {
        'user_form': user_form,
        'student_form': student_form
    })


def student_information(request):
    students = StudentProfile.objects.order_by('-user__is_active', 'user__first_name')
    return render(request, 'student/student_information.html', {'students': students})


def toggle_student_status(request, NUID):
    if request.method == "POST":
        student = get_object_or_404(User, NUID=NUID)
        student.is_active = not student.is_active
        student.save()
    return redirect('student_information')  # Replace with your actual redirect URL


def visit_reason(request):
    if request.method == 'POST':
        form = VisitReasonForm(request.POST)
        if form.is_valid():
            # Associate the visit reason with the logged-in student
            student_profile = request.user.studentprofile
            visit_reason = form.save(commit=False)
            visit_reason.student = student_profile  # Assuming you have a field to link to student
            visit_reason.save()

            # Log out the user after form submission
            logout(request)

            # Redirect to the end page
            return redirect('end_page')
    else:
        form = VisitReasonForm()

    return render(request, 'student/visit_reason.html', {'form': form})

def end_page(request):
    return render(request, 'student/end_page.html')


