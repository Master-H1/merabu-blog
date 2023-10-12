from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("allposts", views.allPostsView.as_view(), name="posts"),
    path("eachpost/<slug:slug>", views.EachPostView.as_view(), name="eachpo"),
    path("read-later", views.ReadLaterView.as_view(), name="readlater")

]
