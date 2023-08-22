from typing import Dict, Any

from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post


# Create your views here.


class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class PostDetailView(DetailView):
    template_name = 'blog/post-details.html'
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
