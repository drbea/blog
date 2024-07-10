from django.shortcuts import render
from rest_framework import generics
from django.db.models import Q
from django.core.paginator import Paginator
from .serializers import CoursSerializer, ProductSerializer, MatiereSerializer, CategorySerializer
from .models import Article, Cours, Product, Matiere, Command, Category
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    # articles = Article.objects.all().order_by('-publication_date')
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    articles = Article.objects.filter(Q(title__icontains = q) |
                                Q(content__icontains=q)|
                                Q(author__icontains=q)).order_by('-publication_date')
    paginator = Paginator(articles, per_page=10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "articles": articles,
        "q": q,
        "page_obj": page_obj,
    }
    return render(request, "blog/index.html", context)




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