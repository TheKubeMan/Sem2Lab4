from articles import models
from django.shortcuts import render
from django.http import Http404
from .models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": models.Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
