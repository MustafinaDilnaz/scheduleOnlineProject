from django import forms

from django.forms import ModelForm
from .models import Administrator
from .models import Employee, Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User


class CreateEmployeeForm(ModelForm):
    name = forms.CharField(label='name', max_length=100)
    surname = forms.CharField(label='surname', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    jobDescription = forms.CharField(label='job Description', max_length=100)
    phoneNumber = forms.CharField(label='phone Number', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    group_id = forms.ModelChoiceField(queryset=Group.objects, label='', empty_label="Choose..")
    administrator = forms.ModelChoiceField(queryset=Administrator.objects, label='', empty_label="Choose..")
    class Meta:
        model = Employee
        fields = ["name", "surname", "password", "email", "jobDescription", "phoneNumber", "group_id", "administrator"]


class CreateClientForm(ModelForm):
    # user = forms.CharField(max_length=100)
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    group_id = forms.ModelChoiceField(queryset=Group.objects, label='', empty_label="Choose..")
    phoneNumber = forms.CharField(label='phone Number', max_length=100)

    class Meta:
        model = Client
        fields = ["name", "surname", "password", "email",  "phoneNumber", "group_id"]



class RegisterForm(ModelForm):
    # user = forms.CharField(max_length=100)
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    group_id = forms.ModelChoiceField(queryset=Group.objects, label='', empty_label="Choose..")

    class Meta:
        model = Administrator
        fields = ["name", "surname", "password", "email", "group_id"]


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']