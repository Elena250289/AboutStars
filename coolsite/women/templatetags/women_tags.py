''' В данном файле создаем пользовательские теги.'''
#(теги нужны для того чтобы не было дублирования кода)
from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    '''
    Тег будет загружать категории из БД
    и использоваться непосредственно в шаблоне
    '''
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    '''
  В функции происходит чтение всех рубрик из БД, 
  а затем, возвращается словарь с этими данными.
    '''
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}
