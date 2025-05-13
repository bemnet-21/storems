from django.db import models
from django.conf import settings

class Stores(models.Model):
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_stores")
    address = models.CharField(max_length=150)
    stock_quantity = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    capacity = models.PositiveIntegerField()
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Store at {self.address}"


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employee_profile")
    address = models.CharField(max_length=150)
    hired_date = models.DateField()
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=100)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_profile")
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name()


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()
    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    TERMS = (
        ("on_delivery", "On Delivery"),
        ("in_advance", "In Advance")
    )
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    payment_terms = models.CharField(max_length=20, choices=TERMS)
    products = models.ManyToManyField(Product, related_name='suppliers')

    def __str__(self):
        return self.name


class Sale(models.Model):
    quantity = models.PositiveIntegerField()
    sale_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name='sales')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='handled_sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')

    def save(self, *args, **kwargs):
        self.total_price = self.product.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sale of {self.product.name} to {self.customer.user.username}"
