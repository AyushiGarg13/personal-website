from django.urls import path

from blog.views import index, post_details, posts

urlpatterns = [
    path("", index, name="index"),
    path("posts", posts, name="post"),
    path("posts/<slug:post_name>", post_details, name="post_details"),
]
