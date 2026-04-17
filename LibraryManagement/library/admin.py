from django.contrib import admin
from library.models import Author,Book,Loan
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Loan)
