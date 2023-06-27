from datetime import date
from django.shortcuts import render

from blog.models import Post

# Create your views here.

all_posts = [
]


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })


def post_details(request, slug):
    post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, 'blog/post-details.html', {
        "post": post
    })
