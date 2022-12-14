from datetime import datetime

from django.db import models
from django.contrib.auth.models import Group
from strategy_field.fields import StrategyField
from strategy_field.registry import Registry


class SingletonModel(models.Model):
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class SuperUser(SingletonModel):
    superUserName = models.CharField(max_length=15)
    password = models.CharField(max_length=15)


class AbstractAddInfo(object):
    def __init__(self, context):
        self.context = context

    def addInfo(self):
        raise NotImplementedError


class AddInfo1(AbstractAddInfo):
    def addInfo(self):
        print("Add information 1")


class AddInfo2(AbstractAddInfo):
    def addInfo(self):
        print("Add information 2")


registry = Registry(AbstractAddInfo)
registry.register(AddInfo1)
registry.register(AddInfo2)


class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    # admin = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    information = StrategyField(registry=registry)

    def __str__(self):
        return f"Name: {self.name} {self.surname}"


# inheritance userClass (userClass)
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    # employee = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    jobDescription = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name} {self.surname}"


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    surname = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"Name: {self.name} {self.surname}"


class Appointment(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    appointmentStartTime = models.DateTimeField()
    appointmentEndTime = models.DateTimeField()
    price = models.FloatField()
    isDoneStatus = models.BooleanField(default=False)

    def get_remaining_time(self):
        today = datetime.date.today()
        return (today.year - self.appointmentStartTime.year) - int(
            (today.month, today.day) <
            (self.appointmentStartTime.month, self.appointmentStartTime.day))
