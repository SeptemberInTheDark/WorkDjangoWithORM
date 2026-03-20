from django.shortcuts import render

from .models import Article

# Create your views here.


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().order_by(ordering).prefetch_related('scopes__tag')
    context = {
        'object_list': articles,
    }
    return render(request, template, context)