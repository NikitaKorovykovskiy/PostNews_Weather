from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = [
        "title",
        "text",
    ]
    list_display = ("title", "author", "pub_date", "image", "text")
    readonly_fields = ["preview"]


admin.site.register(Post, PostAdmin)
