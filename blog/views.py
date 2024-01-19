from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/posts.html"
    paginate_by = 6


def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset)

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
            },
        )