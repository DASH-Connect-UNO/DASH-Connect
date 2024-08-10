from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from DASH_pillars.models import Hardship, BasicNeedSupport, Scholarship
from .models import StudentProfile, AdminProfile, CustomUser, VisitReason
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('NUID', 'user_type', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'email')
        error_messages = {
            'NUID': {'required': ''},
            'user_type': {'required': ''},
            'password1': {'required': ''},
            'password2': {'required': ''},
            'first_name': {'required': ''},
            'middle_name': {'required': ''},
            'last_name': {'required': ''},
            'email': {'required': ''},
        }

class StudentForm(forms.ModelForm):
    YEAR_CHOICES = [
        ('First Year', 'First Year'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate Student', 'Graduate Student'),
        ('Other', 'Other'),
    ]

    year = forms.ChoiceField(choices=YEAR_CHOICES, required=True)
    other_year = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Please specify...'}))

    class Meta:
        model = StudentProfile
        fields = ['DASH_Member', 'year', 'other_year', 'scholarships', 'hardships', 'basic_need_supports']
        error_messages = {
            'DASH_Member': {'required': 'This field is required.'},
            'year': {'required': 'This field is required.'},
            'scholarships': {'required': 'This field is required.'},
            'hardships': {'required': 'This field is required.'},
            'basic_need_supports': {'required': 'This field is required.'},
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['scholarships'].queryset = Scholarship.objects.filter(is_deactivated=False)
        self.fields['hardships'].queryset = Hardship.objects.filter(is_deactivated=False)
        self.fields['basic_need_supports'].queryset = BasicNeedSupport.objects.filter(is_deactivated=False)

    def clean(self):
        cleaned_data = super().clean()
        year = cleaned_data.get('year')
        other_year = cleaned_data.get('other_year')

        if year == 'Other' and not other_year:
            self.add_error('other_year', 'Please specify the other year.')


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'email']  # Exclude password fields
        error_messages = {
            'first_name': {'required': 'This field is required.'},
            'middle_name': {'required': 'This field is required.'},
            'last_name': {'required': 'This field is required.'},
            'email': {'required': 'This field is required.'},
        }


class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['role_within_DASH']
        error_messages = {
            'role_within_DASH': {'required': ''},
        }


class VisitReasonForm(forms.ModelForm):
    class Meta:
        model = VisitReason
        fields = [
            'appointment',
            'printing',
            'study',
            'socialize',
            'event',
            'schedule_appointment',
            'hardship',
            'basic_needs_support',
            'financial_wellness',
            'volunteer_opportunities',
            # 'date_time',  # Make sure this is added correctly
        ]
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
            'date_time': _('Date and Time')  # Make sure this is labeled correctly
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
            'date_time': forms.HiddenInput(),  # Optional: Hide this field from the form
        }

    def clean(self):
        cleaned_data = super().clean()
        if not any(cleaned_data.get(field) for field in self.fields if field != 'date_time'):
            raise forms.ValidationError(_('At least one reason for the visit must be selected.'))





