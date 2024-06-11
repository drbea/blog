from django.shortcuts import render
from rest_framework import generics
from .serializers import CoursSerializer, ProductSerializer, MatiereSerializer, CategorySerializer
from .models import Cours, Product, Matiere, Command, Category
from django.contrib.auth.models import User
# Create your views here.

def index(request):

    context = {
        "message": "Hello, you're at welcome page"
    }
    return render(request, "blog/index.html")

class CoursList(generics.ListCreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class MatiereList(generics.ListCreateAPIView):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer

def profile(request):

    context = {
        "hello": "hellowolrd"
    }
    return render(request, "blog/profile.html")