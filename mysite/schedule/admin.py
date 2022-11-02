# from django.contrib import admin
# from .models import Post
#
# admin.site.register(Post)

from django.contrib import admin
from schedule.models import Administrator, Client, Employee, Appointment, Group

class AdministratorsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Administrator, AdministratorsAdmin)


class ClientsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientsAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)

class AppointmentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentsAdmin)

# class GroupAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Group, AppointmentsAdmin)

