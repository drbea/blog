from django.forms import ModelForm
from .models import Room, Message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]



class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = "__all__"



class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name']
        # fields = "__all__"


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']