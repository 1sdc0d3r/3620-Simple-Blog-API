from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(("name"), max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(("title"), max_length=100)
    author = models.CharField(("author"), max_length=100)
    published_date = models.CharField(("published_date"), max_length=50)

    def __str__(self):
        return self.title

class Loan(models.Model):
    borrower = models.CharField(("borrower"), max_length=100)
    title = models.CharField(("title"), max_length=100)
    loan_date = models.CharField(("loan_date"), max_length=50)

    def __str__(self):
        return self.borrower
