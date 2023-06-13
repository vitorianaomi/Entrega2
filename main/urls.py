"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from curso.views import index, detalhe_curso, lista_cursos, sobre
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name = 'template_index'), 
    path('cursos/', lista_cursos, name = 'lista_cursos'),
    path('detalhecurso/<int:id_curso>', detalhe_curso, name = 'detalhe_curso'),
    path('sobre/', sobre, name = 'template_sobre'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

