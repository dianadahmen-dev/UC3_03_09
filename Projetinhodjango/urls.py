"""
URL configuration for Projetinhodjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from academia import views
from meu_primeiro_app import views

#dia 03.09 nao consegui carregar o estilo. Tentar segunda feira
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_meu_primeiro_app, name ='home'),
    path('contato/', views.contato_meu_primeiro_app, name ='contato'),
    path('produtos/', views.produtos_meu_primeiro_app, name ='produtos'),
    path('', views.home, name ='home1'),
    path('unidades/', views.unidades, name ='unidades'),
    path('contato/', views.contato, name ='contato'),
    path('', views.home1, name ='home1'),
    path('unidades/', views.unidades, name ='unidades'),
    path('contato/', views.contato, name ='contato'),
]
