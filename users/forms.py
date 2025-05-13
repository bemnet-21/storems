from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

ROLE = (
        ('customer', 'Customer'),
        ('employee', 'Employee'),
        ('admin', 'Admin'),
    )
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''

        
    role = forms.ChoiceField(choices=ROLE, widget=forms.Select)
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'phone', 'role']

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role == 'admin' and Users.objects.filter(role='admin').exists():
            raise forms.ValidationError("Admin already exists")
        else:
            return role

