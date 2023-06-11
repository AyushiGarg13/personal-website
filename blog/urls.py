from django.urls import path

from blog.views import index, post_details, posts

urlpatterns = [
    path("", index, name="index"),
    path("posts", posts, name="posts"),
    path("posts/<slug:slug>", post_details, name="post_details"),
]
