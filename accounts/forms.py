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

class VisitReasonForm(forms.Form):
    # One field should be required
    appointment = forms.BooleanField(label='Appointment with DASH staff', required=False)
    printing = forms.BooleanField(label='Printing', required=False)
    study = forms.BooleanField(label='Study', required=False)
    socialize = forms.BooleanField(label='Socialize/Relax', required=False)
    event = forms.BooleanField(label='Event', required=False)

    # Follow-up options
    # Optional
    schedule_appointment = forms.BooleanField(label='Schedule an appointment', required=False)
    hardship = forms.BooleanField(label='Hardship', required=False)
    basic_needs_support = forms.BooleanField(label='Basic Needs Support', required=False)
    financial_wellness = forms.BooleanField(label='Financial Wellness', required=False)
    volunteer_opportunities = forms.BooleanField(label='Volunteer Opportunities', required=False)
