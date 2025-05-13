from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Stores
# Create your views here.
@login_required
def index(request):
    user = request.user

    if user.groups.filter(name="customer").exists():
        return redirect('customer_page')
    elif user.groups.filter(name="employee").exists():
        return redirect('employee_page')
    else:
        return redirect('admin_page')
    
def customer_page(request):
    pass