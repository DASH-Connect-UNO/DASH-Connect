from django.urls import path
from .views import (
    pillars_home, student_information, add_student, list_scholarships, add_scholarship, edit_scholarship, remove_scholarship,
    list_hardships, add_hardship, edit_hardship, remove_hardship,
    list_basic_need_supports, add_basic_need_support, edit_basic_need_support, remove_basic_need_support
)

urlpatterns = [
    path('', pillars_home, name='pillars_home'),


    path('scholarships/', list_scholarships, name='list_scholarships'),
    path('scholarships/add/', add_scholarship, name='add_scholarship'),
    path('scholarships/edit/<int:id>/', edit_scholarship, name='edit_scholarship'),
    path('scholarships/remove/<int:id>/', remove_scholarship, name='remove_scholarship'),
    path('hardships/', list_hardships, name='list_hardships'),
    path('hardships/add/', add_hardship, name='add_hardship'),
    path('hardships/edit/<int:id>/', edit_hardship, name='edit_hardship'),
    path('hardships/remove/<int:id>/', remove_hardship, name='remove_hardship'),
    path('basic_need_supports/', list_basic_need_supports, name='list_basic_need_supports'),
    path('basic_need_supports/add/', add_basic_need_support, name='add_basic_need_support'),
    path('basic_need_supports/edit/<int:id>/', edit_basic_need_support, name='edit_basic_need_support'),
    path('basic_need_supports/remove/<int:id>/', remove_basic_need_support, name='remove_basic_need_support'),
]

