from django.urls import path
from . import views

app_name = "authentification"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register, name="register"),
    path("signin/", views.registerPage, name="register2"),
    path("profile/<str:user_id>/", views.userProfile, name="userProfile"),
    path("update-user/", views.updateUser, name="update-user"),
    
]