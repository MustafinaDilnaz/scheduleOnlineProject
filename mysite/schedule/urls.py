from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views #import this
from .views import (
        createEmployee,
        createAdmin,
        base,
        home,
        createClient,
        register,
        password_reset_request,
        Profile,
        AdministratorsListView,
        ClientsListView,
        EmployeesListView,
        about,
        Table
)


urlpatterns = [
        # path('', home),
        path('about/', about),
        path('createEmployee/', createEmployee, name='my_view'),
        path('createAdmin/', createAdmin, name='register'),
        path('createClient/', createClient, name='createClient'),
        path('api/v1/drf-auth/', include('rest_framework.urls')),
        path('register/', register, name='register'),
        path('accounts/profile/', Profile),
        path('administrators/', AdministratorsListView.as_view()),
        path('employees/', EmployeesListView.as_view()),
        path('clients/', ClientsListView.as_view()),
        path('table/', Table),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),
]
