from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (student_login_view, admin_login_view, admin_profile_view, student_profile, add_admin, edit_admin, remove_admin,
                    remove_student, edit_student)

urlpatterns = [
    path('student_login/', student_login_view, name='student_login'),
    path('admin_login/', admin_login_view, name='admin_login'),
    path('admin_profile/', admin_profile_view, name='admin_profile'),
    path('student_profile/<int:id>/', student_profile, name='student_profile'),
    path('add_admin/', add_admin, name='add_admin'),
    path('edit_admin/<int:id>/', edit_admin, name='edit_admin'),
    path('edit_student/<int:id>/', edit_student, name='edit_student'),
    path('remove_admin/', remove_admin, name='remove_admin'),
    path('remove_student/', remove_student, name='remove_student'),
    path('logout/', LogoutView.as_view(next_page='admin_login'), name='logout'),
]
