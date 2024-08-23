from django.db import models
from django.urls import reverse


class Women(models.Model):
    '''
    Создаем таблицу в базе данных,
    для этого создаем класс с нужными полями
    '''
    # Примечание: verbose_name формируем русскоязычное название
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    content = models.TextField(blank=True,
                               verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",
                              verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    ''' Связываем с таблицей Category'''
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            verbose_name="Категории")

    def __str__(self):
        '''
        def __str__(self) Помогает вернуть
        более описательные данные экземпляра
        '''
        return self.title

    def get_absolute_url(self):
        '''
        Метод возвращает полный URL-адрес для каждой конкретной записи
        Используется функция reverse, которая строит текущий URL-адрес
        записи на основе post.
        '''
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create', 'title']


# Создаем ещё одну таблицу, где будут указаны категории для 1-ой таблицы
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name ='Категория')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
