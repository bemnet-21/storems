from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

# Create your views here.
def login_users(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
    return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        role = request.POST["role"]
        form = CustomUserCreationForm(name, username, email, address, phone, role)

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
        