from django.shortcuts import render
from blog_app.models import Blog

# Create your views here.
def blog_posts(req):
    posts = Blog.objects.all()
    print(posts)

def blog_post(req):
    # req.params.id
    # posts = Blog.objects.all()

    # print(posts)
    pass
