from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return render(request, 'women/addpage.html')


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def register(request):
    return HttpResponse("Regristration")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)


def random_page(request):
    return render(request, 'women/random.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'women/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
