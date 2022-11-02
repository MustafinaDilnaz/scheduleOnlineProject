from django.http import HttpResponseRedirect
from .forms import CreateEmployeeForm, RegisterForm, CreateClientForm
from .models import Administrator, Employee, Client
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.generic import ListView, DetailView
from django.views import generic
from django.forms.models import model_to_dict
import json



# Create your views here.

# getAllUsers, getAllAdministrators. getAllAppointments, getAllClients
# getUser(id), getAdministrator(id), getAppointment(id), getClient(id)
# setUser(id, user), setAdministrator(id, admin), setAppointment(id, appointment), setClient(id, client)


def createEmployee(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            newEmployee = form.save(commit=False)
            newEmployee.admin = request.user
            newEmployee.save()
    else:
        form = CreateEmployeeForm()
    return render(request, 'register.html', {'form': form})


def createClient(request):
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            newClient = form.save(commit=False)
            newClient.admin = request.user
            newClient.save()
    else:
        form = CreateClientForm()
    return render(request, 'register.html', {'form': form})




def createAdmin(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # newAdmin = Administrator(name=form.Meta.fields[0], surname=form.Meta.fields[1], email=form.Meta.fields[2], password=form.Meta.fields[3])
            # print(newAdmin)
            # newAdmin.save()
            newAdmin = form.save(commit=False)
            newAdmin.admin = request.user
            newAdmin.save()
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def Profile(request):
    return render(request, 'profile.html')


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
        password_reset_form = PasswordResetForm()
        return render(request=request, template_name="password/password_reset.html",
                      context={"password_reset_form": password_reset_form})


class AdministratorsListView(ListView):
    model = Administrator
    template_name = 'list.html'


class ClientsListView(ListView):
    model = Client
    template_name = 'list.html'


class EmployeesListView(ListView):
    model = Employee
    template_name = 'list.html'


def Table(request):
    json_records = model_to_dict(Client.objects)
    serialized = json.dumps(json_records)
    data = json.loads(serialized)
    context = {'d':data}
    return render(request, 'table.html', context )
