from django.urls import path

from blog.views import IndexView, PostsView, PostDetailView, ReadLaterView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts", PostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", PostDetailView.as_view(), name="post_details"),
    path("read-later", ReadLaterView.as_view(), name="read_later")
]
