from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (student_login_view, admin_login_view, admin_profile_view, student_profile, add_admin, edit_admin,
                    remove_student, edit_student, admin_list_view, deactivate_admin_view, reactivate_admin_view,
                    register_admin, add_student, student_information, visit_reason)

urlpatterns = [
    path('student_login/', student_login_view, name='student_login'),
    path('admin_login/', admin_login_view, name='admin_login'),
    path('admin_profile/', admin_profile_view, name='admin_profile'),
    path('add_student/', add_student, name='add_student'),
    path('student_information/', student_information, name='student_information'),
    path('student_profile/<str:NUID>/', student_profile, name='student_profile'),
    path('add_admin/', add_admin, name='add_admin'),
    path('edit_admin/<str:NUID>/', edit_admin, name='edit_admin'),  # Updated this line
    path('edit_student/<str:NUID>/', edit_student, name='edit_student'),
    path('admin_list/', admin_list_view, name='admin_list'),
    path('deactivate_admin/', deactivate_admin_view, name='deactivate_admin'),
    path('reactivate_admin/', reactivate_admin_view, name='reactivate_admin'),
    path('remove_student/', remove_student, name='remove_student'),
    path('logout/', LogoutView.as_view(next_page='admin_login'), name='logout'),
    path('register_admin/', register_admin, name='register_admin'),
    path('visit_reason/', visit_reason, name='visit_reason'),
]

