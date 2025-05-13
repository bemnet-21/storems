from django.db import models

ROLE = (
    ('customer', 'Customer'),
    ('employee', 'Employee'),
    ('admin', 'Admin'),
)

class Users(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=17)
    role = models.CharField(max_length=10, choices=ROLE, default='customer')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = []

    def __str__(self):
        return self.username
