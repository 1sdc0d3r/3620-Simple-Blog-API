from django.shortcuts import render
from blog_app.models import Blog
from django.http import JsonResponse

# Create your views here.
def blog_posts(req):
    posts = Blog.objects.all()
    # print(posts.values())
    data = {
        'posts': list(posts.values())
    }

    return JsonResponse(data)

def blog_post(req, id):
    post = Blog.objects.get(pk=id)

    data = {
        'title': post.title,
        'content': post.content,
        'published_date': post.published_date,
    }
    return JsonResponse(data)
