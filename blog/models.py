from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)


class Command(models.Model):

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey("blog.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)


class Matiere(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Cours(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField(null = True, blank = True)
    matiere = models.ForeignKey("blog.Matiere", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Product(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(null = True, blank = True)
    category = models.ForeignKey("blog.Category", on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateTimeField()
    url = models.URLField()
    url_to_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
   