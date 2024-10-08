#  Убираем дублирование кода из классов представлений
from django.db.models import Count

from .models import *

# Переносим сюда  главное меню,
# т.к. оно используется напрямую классом DataMixin
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 2
    '''Благодаря этому методу -get_user_context, нам не придется в классах
     представлений каждый раз прописывать ссылки на главное меню и категории'''
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
