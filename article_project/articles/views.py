from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles.html', {'articles': articles})


def article_create(request):
    if request.method == 'POST':
        # Получаем данные из формы
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        # Валидация
        if title and content:
            article = Article.objects.create(
                title=title,
                content=content
            )
            return redirect('article_list')
        else:
            # Если валидация не прошла, показываем форму с ошибкой
            return render(request, 'create.html', {
                'error': 'Заполните все поля',
                'title': title,
                'content': content
            })

    # GET запрос - показываем пустую форму
    return render(request, 'create.html')


def article_edit(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        # Получаем данные из формы
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        # Валидация
        if title and content:
            article.title = title
            article.content = content
            article.save()
            return redirect('article_list')
        else:
            # Если валидация не прошла, показываем форму с ошибкой
            return render(request, 'edit.html', {
                'article': article,
                'error': 'Заполните все поля',
                'title': title,
                'content': content
            })

    # GET запрос - показываем форму с данными статьи
    return render(request, 'edit.html', {'article': article})