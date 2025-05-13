from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def login_users(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store:index')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, "users/register.html", {
                "form": form
            })
    else:
        return render(request, "users/register.html", {
            "form": CustomUserCreationForm()
        })
        

def user_logout(request):
    logout(request)
    return redirect('users:login')