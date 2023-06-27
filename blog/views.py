from django.shortcuts import render, get_object_or_404

from blog.models import Post

# Create your views here.

all_posts = Post.objects.all()


def index(request):
    latest_posts = all_posts.order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts.order_by("-date")
    })


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-details.html', {
        "post": post,
        "post_tags": post.tags.all()
    })
