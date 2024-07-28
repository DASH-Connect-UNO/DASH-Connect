from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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
                return redirect('admin_dashboard')  # Change to your admin dashboard URL
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/admin_login.html', {'form': form})

def admin_profile_view(request):
    # You can add any context here if needed
    context = {}
    return render(request, 'accounts/admin_profile.html', context)

