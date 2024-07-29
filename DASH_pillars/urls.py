from django.urls import path
from . import views

urlpatterns = [
    path('', views.pillars_home, name='pillars_home'),
    path('scholarships/', views.list_scholarships, name='list_scholarships'),
    path('scholarships/add/', views.add_scholarship, name='add_scholarship'),
    path('scholarships/remove/<int:id>/', views.remove_scholarship, name='remove_scholarship'),
    path('scholarships/edit/<int:id>/', views.edit_scholarship, name='edit_scholarship'),
    path('hardships/', views.list_hardships, name='list_hardships'),
    path('hardships/add/', views.add_hardship, name='add_hardship'),
    path('hardships/remove/<int:id>/', views.remove_hardship, name='remove_hardship'),
    path('hardships/edit/<int:id>/', views.edit_hardship, name='edit_hardship'),
    path('basic_need_supports/', views.list_basic_need_supports, name='list_basic_need_supports'),
    path('basic_need_supports/add/', views.add_basic_need_support, name='add_basic_need_support'),
    path('basic_need_supports/remove/<int:id>/', views.remove_basic_need_support, name='remove_basic_need_support'),
    path('basic_need_supports/edit/<int:id>/', views.edit_basic_need_support, name='edit_basic_need_support'),
]


