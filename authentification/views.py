from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
    
        user = User.objects.create_user(username = username, email = email, password = password)
        user.first_name = first_name
        user.last_login = last_name
        user.save()

        if User.objects.filter(username = username):
            messages.error(request, "username already exists")
            return redirect("authentification:register")
        
        if User.objects.filter(email = email):
            messages.error(request, "email already exists")
            return redirect("authentification:register")
        
        if not username.isalnum():
            messages.error(request, "username should only contain letters and numbers")
            return redirect("authentification:register")
        
        if password != password2:
            messages.error(request, "password do not match")
            return redirect("authentification:register")

        messages.success(request, "you have been sigin succesfully")
        return redirect("authentification:login")

    return render(request, "authentification/register.html")


def login_user(request):

    if request.method == "POST":
        password = request.POST.get("password")
        username = request.POST.get("username")

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged successfully")
            return render(request, "blog/index.html")
        else:
            messages.error(request, "les donnees fournies sont incorrectes !!!")
            return redirect("authentification:login")


    return render(request, "authentification/login.html")
    
    
    
        

def logout_user(request):
    logout(request)
    messages.success(request, "Deconnexion reuissie ...")
    return redirect("blog:home")