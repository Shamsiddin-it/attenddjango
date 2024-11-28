from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email')

from django import forms
from .models import Attendence

class AttendanceSearchForm(forms.Form):
    student_name = forms.CharField(required=False, label='Student Name')
    status = forms.ChoiceField(
        choices=[('', 'All'), ('came', 'Came'), ('late', 'Late'), ('absent', 'Absent'), ('left', 'Left')],
        required=False,
        label='Status'
    )
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='From Date')
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='To Date')
