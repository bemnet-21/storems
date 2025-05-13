from django.db import models

# Create your models here.
class Stores(models.Model):
    address = models.CharField(max_length=150)
    stock_quantity = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    capacity = models.PositiveIntegerField()
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    last_updated = models.DateTimeField()

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    hired_date = models.DateField()
    phone = models.CharField()
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=100)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name="employees")

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    phone = models.CharField()
    email = models.EmailField()

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()

    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name="products")

class Supplier(models.Model):
    TERMS = (
        ("on_delivery", "On Delivery"),
        ("in_advance", "In Advance")
    )
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    phone = models.CharField()
    email = models.EmailField()
    payment_terms = models.CharField(max_length=20, choices=TERMS)
    product = models.ManyToManyField(Product, related_name='suppliers')
class Sale(models.Model):
    quantity = models.PositiveIntegerField()
    sale_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name='sales')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='handled_sales')
    product = models.ManyToManyField(Product, related_name='sales')