# rest-apis

Nesse repositório estarei explicando, de uma maneira simples, o passo a passo para criar uma **REST API**, utilizando o **Django** e o **Django REST framework**. Optei por escrever esse tutorial em português, pois é um tópico bastante requisitado e que não se encontra tanto conteúdo assim no nosso idioma. 

**IMPORTANTE:** Recomenda-se ter um conhecimento mínimo em **Django**, pois passarei direto pelas explicações de conceitos básicos, apenas executando comandos tendo em mente que você, leitor, sabe o que está acontecendo.

Para facilitar a sua leitura e o seu entendimento, dividi esse tutorial em vários passos.

1. Iniciando o projeto **Django**.
2. Iniciando uma aplicação.
3. Instalando o **Django REST framework**.
4. Criando o modelo.
5. Migrando as aplicações.

## 1. Iniciando o projeto Django

Para iniciar um novo projeto, primeiramente você deve ter o framework **Django** instalado em sua máquina (no momento em que estou escrevendo isso, a versão mais recente é a `3.2.7`, recomendo que instale essa, ou caso exista, uma superior, sempre preferindo trabalhar em um ambiente virtual próprio para o projeto), para instalá-lo você pode simplesmente digitar em seu terminal:

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

A diferença entre projeto e aplicação nem sempre é muito bem entendida, uma ótima definição está presente na própria [documentação](https://docs.djangoproject.com/pt-br/3.2/intro/tutorial01/#write-your-first-view) do **Django**.

> Qual é a diferença entre um projeto e uma aplicação? Uma aplicação é um conjunto de elementos web que faz alguma coisa - por exemplo, um sistema de blog, um banco de dados de registros públicos, ou uma pequena aplicação de enquetes. Um projeto é uma coleção de configurações e aplicações para um website particular. Um projeto pode conter múltiplas aplicações. Uma aplicação pode estar em múltiplos projetos. Em Django, chamamos uma aplicação de “app”.

Logo após a criação de sua aplicação, você deverá adicioná-la ao projeto, acessando as configurações do projeto `settings.py` e acrescentando em `INSTALLED_APPS`, assim o **Django** incluirá a sua aplicação no projeto.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapi.apps.MyapiConfig',  # A aplicação que você acabou de criar
]
```

As aplicações já presentes são padrões do **Django**, fique a vontade para remover as que não são úteis para você.

## 3. Instalando o Django REST framework

Agora que os o projeto e a aplicação foram criados. Vamos instalar o **Django REST framework**.

```sh
pip install djangorestframework
```

E já adicioná-lo na lista de aplicações do nosso projeto.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapi.apps.MyapiConfig',
    'rest_framework',  # Django REST framework
]
```

## 4. Criando o modelo

Para facilitar todo o entendimento e como a criação de modelos e a configuração de bancos de dados não é o nosso foco, usarei o banco de dados padrão do **Django** (`SQLite`) e criarei um modelo bem simples.

O modelo que irei criar se chamará *Person* e contará com quatro campos (cinco, considerando o *id*): *Name*, *Age*, *Height* e *Weight*. Como sabemos, modelos são criados em `models.py`, herdando a classe `django.db.models.Model`.

```python
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
```

Logo após isso, você deve registrar o seu modelo em `admin.py`, pois iremos adicionar novos registros na parte da administração do site. O prórpio **Django REST framework** ja nos disponibiliza uma interface para tal, veremos mais a frente.

```python
from django.contrib import admin
from . import models

admin.site.register(models.Person)
```

## 5. Migrando as aplicações

Antes de migarar as aplicações, tente rodar o seu site e veja o que acontece.

```sh
python manage.py runserver
```

Um aviso apareceu:

```text
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

Todas essas aplicações, que ja foram vistas anteriormente como sendo as padrões do **Django**, estão prontas para serem migradas para o projeto, note que a criado por você não está aí. Usaremos o `makemigrations` para isso, nesse caso, esse comando dirá ao **Django** que temos um novo modelo e queremos que ele fique salvo como uma migração.

```sh
python manage.py makemigrations
```

Pronto, observe que uma pasta chamada `migrations` foi criada, e dentro dela existe o arquivo `0001_initial.py`.

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
                ('height', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
```
