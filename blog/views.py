from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        "message": "Hello, you're at welcome page"
    }
    return render(request, "blog/index.html")