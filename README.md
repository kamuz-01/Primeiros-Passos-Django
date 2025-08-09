# Requisitos

* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version
* GIT - Conferir a instalação: git -v

## Sequencia para criar o projeto

### Criar o ambiente virtual

* python -m venv venv


### Ativar o ambiente virtual

* venv\Scripts\Activate


### Com o venv ativado, instalar o Django

* pip install Django


### Criar o projeto com Django

* django-admin startproject meu_site .


### Criar app pagina_inicial

* python manage.py startapp pagina_inicial


### Configurar o projeto (views e rotas)

#### Adicionar 'pagina_inicial' ao INSTALLED_APPS em meu_site/settings.py

```
INSTALLED_APPS = [
    ...
    'pagina_inicial',
]
```

#### Crie as views em pagina_inicial/views.py

```
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à Home!")

def contato(request):
    return HttpResponse("Página de Contato")
```


### Crie pagina_inicial/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('contato/', views.contato),
]
```

### Atualize meu_site/urls.py

```
from django.urls import path, include

urlpatterns = [
    path('', include('pagina_inicial.urls')),
]

```

## Como rodar o projeto baixado

* python manage.py runserver


## Acessar às páginas criadas com Django.

* http://127.0.0.1:8000/home/


*http://127.0.0.1:8000/contato/

