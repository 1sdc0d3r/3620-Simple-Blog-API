from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(("title"), max_length=50, default="")
    content = models.CharField(("content"), max_length=254, default="")
    published_date = models.CharField(("published_date"), max_length=50, default="")

    def __str__(self):
        return self.title
