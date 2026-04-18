from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(("name"), max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(("title"), max_length=100)
    published_date = models.CharField(("published_date"), max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return self.title

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loan', null=True)
    borrower = models.CharField(("borrower"), max_length=100)
    loan_date = models.CharField(("loan_date"), max_length=50)
    # loan_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.borrower
