from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag, Comment
from django.views.generic import ListView
from django.views.generic.base import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class IndexView(ListView):
    template_name = "index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "latest_posts"

    def get_queryset(self) -> QuerySet[Any]:
        latest = super().get_queryset()
        latest_posts = latest[:3]
        return latest_posts


class allPostsView(ListView):
    template_name = "allposts.html"
    model = Post
    ordering = "-date"
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class EachPostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts

        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post_tags = post.tags.all()
        comment_form = CommentForm()

        context = {"post_tags": post_tags,
                   "comments": post.comments.all(),
                   "saved_for_later": self.is_stored_post(request, post.id),
                   "comment_form": comment_form, "post": post}
        return render(request, "eachpost.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("eachpo", args=[slug]))

        post_tags = post.tags.all()
        context = {"post_tags": post_tags,
                   "comments": post.comments.all(),
                   "saved_for_later": self.is_stored_post(request, post.id),
                   "comment_form": comment_form, "post": post}
        return render(request, "eachpost.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False

        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "stored_posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")
