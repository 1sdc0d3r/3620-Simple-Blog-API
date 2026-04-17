from django.db import models

# Create your models here.
class Blog(models.Model):
    models.CharField(("title"), max_length=50)
    models.CharField(("content"), max_length=254)
    models.CharField(("published_date"), max_length=50)
