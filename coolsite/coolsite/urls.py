"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from women.views import *
from coolsite import settings

# Прописываем пути (передаем весь список URL-адресов приложения
# и связанные с ними функции)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]

# Симуляция работы реального сервера для получения
# ранее загруженных файлов и передачи их нашему приложению
# (на реальных серверах этот процесс, как правило, уже настроен)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Ссылка на функцию, которая и
# будет формировать ответ для отсутствующих страниц
handler404 = pageNotFound
