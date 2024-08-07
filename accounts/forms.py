from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, AdminProfile, CustomUser

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('NUID', 'user_type', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'email')

#Student Profile
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
        fields = [
            'DASH_Member', 'year', 'other_year', 'scholarships', 'hardships', 'basic_need_supports'
        ]

    def clean(self):
        cleaned_data = super().clean()
        year = cleaned_data.get('year')
        other_year = cleaned_data.get('other_year')

        if year == 'Other' and not other_year:
            self.add_error('other_year', 'Please specify the other year.')

#Admin Profile
class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['role_within_DASH']

# Form for deactivating an admin
class DeactivateAdminForm(forms.Form):
    admin_NUID = forms.IntegerField()

# Form for reactivating an admin
class ReactivateAdminForm(forms.Form):
    admin_NUID = forms.IntegerField()
