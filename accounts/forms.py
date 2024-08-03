from django import forms
from .models import Student, Admin


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'middle_name', 'last_name', 'NUID', 'email', 'year',
            'is_dash_member', 'scholarships', 'hardships', 'basic_need_supports']

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['first_name', 'middle_name', 'last_name', 'NUID', 'email', 'role_within_dash']

class RemoveAdminForm(forms.Form):
    nuid = forms.CharField(max_length=20)
    confirm_nuid = forms.CharField(max_length=20)

