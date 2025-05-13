from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE = (
    ('customer', 'Customer'),
    ('employee', 'Employee'),
    ('admin', 'Admin'),
)

class Users(AbstractUser):
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=17)
    role = models.CharField(max_length=10, choices=ROLE, default='customer')

    def __str__(self):
        return self.username

    def get_full_name(self):
        return super().get_full_name()