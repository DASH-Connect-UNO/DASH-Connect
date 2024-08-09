from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, AdminProfile, CustomUser, VisitReason
from django.utils.translation import gettext_lazy as _

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
<<<<<<< Updated upstream

class VisitReasonForm(forms.ModelForm):
    class Meta:
        model = VisitReason
        fields = ['appointment', 'printing', 'study', 'socialize', 'event', 'schedule_appointment', 'hardship',
                  'basic_needs_support', 'financial_wellness', 'volunteer_opportunities']
        labels = {
            'appointment': _('Appointment with DASH staff'),
            'printing': _('Printing'),
            'study': _('Study'),
            'socialize': _('Socialize/Relax'),
            'event': _('Event'),
            'schedule_appointment': _('Schedule an appointment'),
            'hardship': _('Hardship'),
            'basic_needs_support': _('Basic Needs Support'),
            'financial_wellness': _('Financial Wellness'),
            'volunteer_opportunities': _('Volunteer Opportunities'),
        }

        widgets = {
            'appointment': forms.CheckboxInput(),
            'printing': forms.CheckboxInput(),
            'study': forms.CheckboxInput(),
            'socialize': forms.CheckboxInput(),
            'event': forms.CheckboxInput(),
            'schedule_appointment': forms.CheckboxInput(),
            'hardship': forms.CheckboxInput(),
            'basic_needs_support': forms.CheckboxInput(),
            'financial_wellness': forms.CheckboxInput(),
            'volunteer_opportunities': forms.CheckboxInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not any(cleaned_data.get(field) for field in self.fields):
            raise forms.ValidationError(_('At least one reason for the visit must be selected.'))

