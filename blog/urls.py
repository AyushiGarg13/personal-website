from django.urls import path

from blog.views import IndexView, PostsView, PostDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts", PostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", PostDetailView.as_view(), name="post_details"),
]
