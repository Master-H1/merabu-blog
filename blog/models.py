from django.db import models
from django.utils.text import slugify
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog_photo', null=True)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    username = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
