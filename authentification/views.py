from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from room.models import Topic #, Message, Room
from room.forms import UserForm, MyUserCreationForm

# from room.models import Room, User

# Create your views here.

def register(request):
    page = "login"
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

    return render(request, "authentification/register.html", {})


def login_user(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("blog:home")
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


    return render(request, "room/login_user.html", {"page": page})
    # return render(request, "authentification/login.html")
    
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "Deconnexion reuissie ...")
    return redirect("blog:home")

def userProfile(request, user_id):
    user = User.objects.get(id=user_id)
    topics = Topic.objects.all()
    room_messages = user.message_set.all().order_by("-created")
    rooms = user.room_set.all()
    context = {
        "user": user, "rooms": rooms, "topics": topics,
        "room_messages": room_messages,
    }
    return render(request, "room/profile.html", context)


@login_required(login_url="room:login")
def updateUser(request):
    # user = User.objects.get()
    user = request.user
    form = UserForm(instance= user)
    if request.method == "POST":
        form = UserForm(request.POST, instance= user)
        form.save()

        return redirect("authentification:userProfile", user_id= user.id)

    context = {
        # "user": user,
        "form": form
    }
    return render(request, "room/updateUser.html", context)


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'room/login_user.html', {'form': form})

