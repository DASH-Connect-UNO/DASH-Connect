from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import student_login_view, admin_login_view, admin_profile_view

urlpatterns = [
    path('student_login/', student_login_view, name='student_login'),
    path('admin_login/', admin_login_view, name='admin_login'),
    path('admin_profile/', admin_profile_view, name='admin_profile'),
    path('logout/', LogoutView.as_view(next_page='admin_login'), name='logout'),
]
