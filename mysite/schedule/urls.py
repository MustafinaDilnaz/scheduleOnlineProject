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
        about,
        TableClients,
        TableEmployees,
        TableAdministrators,
        deleteClient,
        deleteAdmin,
        deleteEmployee,
        createAppointment,
        calendar,
        deleteAppointment

)


urlpatterns = [
        # path('', home),
        path('about/', about),
        path('createEmployee/', createEmployee, name='my_view'),
        path('createAdmin/', createAdmin, name='register'),
        path('createClient/', createClient, name='createClient'),
        path('createAppointment/', createAppointment, name='createClient'),
        path('api/v1/drf-auth/', include('rest_framework.urls')),
        path('register/', register, name='register'),
        path('accounts/profile/', Profile),
        path('administrators/', TableAdministrators),
        path('employees/', TableEmployees),
        path('clients/', TableClients),
        path('calendar/', calendar),
        path('clients/delete/<str:name>', deleteClient, name='deleteClient'),
        path('employees/delete/<str:name>', deleteEmployee, name='deleteEmployee'),
        path('administrators/delete/<str:name>', deleteAdmin, name='deleteAdmin'),
        path('calendar/delete/<int:pk>', deleteAppointment, name='deleteAdmin'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),
]
