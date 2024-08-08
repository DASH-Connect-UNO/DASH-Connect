from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, AdminProfile, CustomUser

# Get the user model
User = get_user_model()

# Custom user creation form for handling user creation
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('NUID', 'user_type', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'email')

# Form for student profile
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            'DASH_Member', 'year', 'scholarships', 'hardships', 'basic_need_supports'
        ]

# Form for admin profile
class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['role_within_DASH']

# Form for deactivating an admin
class DeactivateAdminForm(forms.Form):
    admin_id = forms.IntegerField()

# Form for reactivating an admin
class ReactivateAdminForm(forms.Form):
    admin_id = forms.IntegerField()
