from django.contrib import admin
from .models import Tag, Author, Post, Comment
# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)


admin.site.register(Post, PostAdmin)
