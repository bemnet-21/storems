from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Stores
# Create your views here.
@login_required
def index(request):
    user = request.user

    if user.groups.filter(name="customer").exists():
        return redirect('store:customer_page')
    elif user.groups.filter(name="employee").exists():
        return redirect('store:employee_page')
    else:
        return redirect('store:admin_page')
    
@login_required
def customer_page(request):
    stores = Stores.objects.all()
    return render(request, "store/customer_page.html", {
        "stores": stores
    })

@login_required
def employee_page(request):
    stores = Stores.objects.all()
    return render(request, "store/customer_page.html", {
        "stores": stores
    })

@login_required
def admin_page(request):
    stores = Stores.objects.all()
    return render(request, "store/admin_page.html", {
        "stores": stores
    })

