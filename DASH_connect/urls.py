from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the current directory if you have any

urlpatterns = [

    # If you want to go to the accounts section of urls, you need something like
    # http://127.0.0.1:8000/accounts/admin_login

    path('admin/', admin.site.urls), # THIS IS A REQUIRED DJANGO DEFAULT FOR THE DJANGO ADMIN PAGE
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
    path('', views.home, name='home'),  # Add a root URL view
    path('pillars/', include('DASH_pillars.urls')),

]
