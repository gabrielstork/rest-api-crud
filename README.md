# rest-api-crud


https://user-images.githubusercontent.com/86558706/134972559-939fab32-1ce2-420b-a96f-e263ab860156.mp4


Nesse repositório estarei explicando, de uma maneira simples, o passo a passo para criar uma **REST API**, utilizando o **Django** e o **Django REST framework**. Optei por escrever esse tutorial em português, pois é um tópico bastante requisitado e que não se encontra tanto conteúdo assim no nosso idioma.

Para facilitar a sua leitura e o seu entendimento, dividi esse tutorial em vários passos.

1. Iniciando o projeto **Django**.
2. Iniciando uma aplicação.
3. Instalando o **Django REST framework**.
4. Criando o modelo.
5. Migrando as aplicações.
6. Definindo *serializers*.
7. Definindo *viewsets*.
8. Definindo *routers*.

**IMPORTANTE:** Para acompanhar esse passo a passo, recomenda-se ter um conhecimento mínimo em **Django**, pois passarei direto pelas explicações de conceitos básicos, tendo em mente que você, leitor, sabe o que está acontecendo.

## 1. Iniciando o projeto Django

Para iniciar um novo projeto, primeiramente você deve ter o framework **Django** instalado em sua máquina (no momento em que estou escrevendo isso, a versão mais recente é a 3.2, recomendo que instale essa, ou caso exista, uma superior, sempre preferindo trabalhar em um ambiente virtual próprio para o projeto), para instalá-lo você pode simplesmente digitar em seu terminal:

```sh
pip install django
```

Depois de instalar o **Django** você deverá criar o seu projeto, no meu caso, o chamarei de `myproject`. 

```sh
django-admin startproject myproject
```

## 2. Iniciando uma aplicação

Depois do projeto ter sido criado, você deverá entrar no diretório do mesmo, pois lá encontra-se o arquivo `manage.py` e é com ele que faremos praticamente tudo a partir de agora.

```sh
cd myproject
```

Com esse arquivo, estarei criando uma aplicação chamada `myapi`.


```sh
python manage.py startapp myapi
```

A diferença entre um projeto e uma aplicação nem sempre é muito bem entendida por quem está começando agora, uma ótima definição está presente na própria [documentação em português](https://docs.djangoproject.com/pt-br/3.2/intro/tutorial01/) do **Django**.

> Qual é a diferença entre um projeto e uma aplicação? Uma aplicação é um conjunto de elementos web que faz alguma coisa - por exemplo, um sistema de blog, um banco de dados de registros públicos, ou uma pequena aplicação de enquetes. Um projeto é uma coleção de configurações e aplicações para um website particular. Um projeto pode conter múltiplas aplicações. Uma aplicação pode estar em múltiplos projetos. Em Django, chamamos uma aplicação de “app”.

Logo após a criação da sua aplicação, você deverá adicioná-la ao projeto, acessando as configurações do projeto `myproject/settings.py` e acrescentando em `INSTALLED_APPS`, assim o **Django** saberá que deve incluir a mesma.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapi.apps.MyapiConfig', # A aplicação que você acabou de criar
]
```

As aplicações já presentes nessa lista são padrões do **Django**, fique a vontade para remover as que não são úteis para você.

## 3. Instalando o Django REST framework

Agora que o projeto e a aplicação foram criados, vamos instalar o **Django REST framework**.

```sh
pip install djangorestframework
```

E já adicioná-lo na lista das aplicações do nosso projeto, repetindo o processo final do item anterior.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapi.apps.MyapiConfig',
    'rest_framework', # Django REST framework
]
```

## 4. Criando o modelo

Para facilitar todo o entendimento e como a criação de modelos e a configuração de bancos de dados não é o nosso foco, usarei o banco de dados padrão do **Django** (`SQLite`) e criarei um modelo bem simples.

O modelo que irei criar se chamará *Person* (pessoa) e contará com quatro campos (cinco, considerando o *id*): *Name* (o nome da pessoa), *Age* (a idade da pessoa), *Country* (o país em que essa pessoa vive atualmente) e *Programmer* (se essa pessoa trabalha ou não com programação). Como sabemos, modelos são criados no arquivo `models.py` das aplicações (no meu caso `myapi/models.py`), herdando a classe `django.db.models.Model`.

```python
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=100)
    programmer = models.BooleanField()
```

Note que os campos que criamos são atributos da classe, cada campo é uma coluna no nosso banco de dados, mas do jeito que está agora ele não tem quase nenhuma utilidade. Precisamos migrá-lo para o nosso projeto de fato.

## 5. Migrando as aplicações

Antes de migrar as aplicações, tente rodar localmente o servidor e veja o que acontece.

```sh
python manage.py runserver
```

Um aviso aparece:

```text
You have 18 unapplied migration(s). Your project may not work properly until you apply
the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

Todas essas aplicações, que já foram vistas anteriormente como sendo as padrões do **Django**, estão prontas para serem migradas para o projeto com um simples `migrate`, note que a criada por você não está aí. Usaremos o `makemigrations` para isso. Nesse caso, esse comando dirá ao **Django** que temos um novo modelo e queremos que ele fique salvo como uma migração.

```sh
python manage.py makemigrations
```

Agora rode o servidor novamente e veja o novo aviso que aparece.

```text
You have 19 unapplied migration(s). Your project may not work properly until you apply
the migrations for app(s): admin, auth, contenttypes, myapi, sessions.
Run 'python manage.py migrate' to apply them.
```

Sua aplicação agora está ali, e o seu modelo pronto para ser migrado. Observe que o diretório `myapi/migrations` foi criado, e dentro dele existe o arquivo `0001_initial.py`.

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=100)),
                ('programmer', models.BooleanField()),
            ],
        ),
    ]
```

Esse é o modelo que criei, (caso você tenha seguido os mesmos passos até aqui, estará assim para você também) salvo e pronto para ser migrado. Caso você tenha alguma experiência com o **git**, o comando `makemigrations` do **Django** funciona da mesma forma que o `add`, assim como o `migrate`, que usaremos agora para migrar de fato as aplicações para o projeto, e o `commit`.

```sh
python manage.py migrate
```

## 6. Definindo serializers

Para explicar a função dos *serializers* adicionarei dois registros no banco de dados criado, pelo próprio terminal do **Django**. Para isso, utilizarei o comando `python manage.py shell`.

```text
python manage.py shell

>>> from myapi.models import Person
>>> person1 = Person(name='João', age=22, country='Brazil', programmer=False)
>>> person1.save()
>>> person2 = Person(name='Maria', age=25, country='Brazil', programmer=True)
>>> person2.save()
>>> Person.objects.all()

<QuerySet [<Person: Person object (1)>, <Person: Person object (2)>]>
```

Você provalvelmente entendeu o que aconteceu, importei o nosso modelo, que é uma classe, criei duas instâncias (`person1` e `person2`) e utilizei o método `save()` para salvá-las como registros no nosso banco de dados, após isso, visualizei todos os objetos presentes no nosso banco de dados com `Person.objects.all()`, e foi retornada uma `QuerySet`, que é um tipo de dado não nativo do **Python**, os *serializers* nos permitem transformar esse tipo de dado em, por exemplo, `json`, e vice-versa.

Para isso, crie um arquivo, no diretório da sua aplicação, chamado `serializers.py`, nele você importará o módulo `serializer` do **Django REST framework** e os seus modelos.

```python
from rest_framework import serializers
from . import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'
```

Note que nome da classe é a junção do nome do modelo que criei e *serializer* (é apenas uma convenção, não necessária mas importante), e herda a classe `rest_framework.serializers.ModelSerializer`, dentro dela você deve criar uma classe `Meta` e definir dois atributos: `model` (o seu modelo) e `fields` (nesse caso eu utilizei `__all__` para pegar todos os campos do meu banco de dados, mas você pode escolher manualmente, especificando-os em uma tupla).

## 7. Definindo viewsets

```python
from rest_framework import viewsets
from . import serializers
from . import models


class PersonViewSets(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
```

## 8. Definindo routers

Como estamos usando *viewsets*, não é preciso definir as configurações de rotas manualmente, a classe `rest_framework.routers.DefaultRouter` fará isso para nós, basta que você a importe, a instancie, e registre suas *viewsets*.

Para isso, crie o arquivo `routers.py` no diretório do seu projeto (no meu caso `myproject/routers.py`).

```python
from rest_framework import routers
from myapi import viewsets

router = routers.DefaultRouter()
router.register('myapi', viewsets.PersonViewSets)
```

Após isso, vá em `myproject/urls.py`, esse arquivo ja deve ser bem conhecido por você, a função `include` deve ser importada do módulo `django.urls`, e você deverá adicionar um item na lista `urlpatterns`. Note que o projeto agora incluirá as suas rotas registradas no arquivo anterior.

```python
from django.contrib import admin
from django.urls import path, include
from . import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.router.urls)),
]
```

