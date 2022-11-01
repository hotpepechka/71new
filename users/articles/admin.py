from django.contrib import admin
from .models import Article
from .models import Comment
from . import models


class CommentInline(admin.TabularInline):
    model = models.Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
# Register your models here.
