"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core.paginator import Paginator

import Blog.My_Blog

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    posts_list = Blog.My_Blog.models.Post.objects.all()
    
    # обрезаю текст поста
    for post in posts_list:
        post.text = post.text[:100] + '...'

    paginator = Paginator(posts_list, 5)
    
    page_number = None    

    # Получаю page_number для отображения paginator-ом
    if '/page/' in request.path:
        try:
            url = request.path
            url = url[6:]
            page_number = int(url)
        except:
            page_number = 1 
    else: page_number = 1

    posts_list = paginator.page(page_number)

    #Список выглядит так 1,2, ... num_pages
    pages_bar = [i+1 for i in range(paginator.num_pages)]
  
    
    # Удаляю некоторые елементы из списка что б не выводить слишком много ссылок на страницы
    if len(pages_bar) > 6:
        for number in range(len(pages_bar)):
            if (number > 2) and (number < paginator.num_pages - 1) and ( number not in [page_number-1, page_number, page_number+1] ):
                pages_bar.remove(number)
        # добавляю '...'        
        for number in range(len(pages_bar)):
            try:
                if pages_bar[number] - pages_bar[number-1] > 1:
                    pages_bar.insert(number, '...')
            except:
                do = 'nothing'

    for post in posts_list:
        if post.image == None:
            print('oh shit')

    return render(
        request,
        'app/index2.html',
        {
            'pages_bar':pages_bar,
            'posts_list':posts_list,
            'current_page':page_number,
            'title':'Домашняя страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Об авторе',
            'message':'',
            'year':datetime.now().year,
        }
    )

def post(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    number = None
    if request.method == 'GET':
        number = request.GET['id'] 
    post = Blog.My_Blog.models.Post.objects.get(id=number)

    return render(
        request,
        'app/post.html',
        {
            'title':'Пост '+post.title,
            'post':post,
            'year':datetime.now().year,
        }
    )