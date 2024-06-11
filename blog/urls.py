from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name = "home"),
    path("cours/", views.CoursList.as_view(), name = "cours"),
    path("matiere/", views.MatiereList.as_view(), name = "matiere"),
    # path("product/", views.ProductList.as_view(), name = "product"),

    path("profil/", views.profile, name ="profile")
]
