# rest-apis

Nesse repositório estarei explicando, de uma maneira simples, o passo a passo sobre como criar uma **REST API**, utilizando o **Django** e o **Django REST framework**. Optei por escrever esse tutorial em português, pois é um tópico bastante requisitado e que não se encontra tanto conteúdo assim no nosso idioma. 

**IMPORTANTE:** Recomenda-se ter um conhecimento mínimo em **Django**, pois passarei direto por explicações de conceitos básicos, apenas executando comandos tendo em mente que você, leitor, sabe o que está acontecendo.

Para facilitar a leitura e o seu entendimento, dividi esse tutorial em vários passsos.

1. Iniciando o projeto **Django**.
2. Iniciando uma aplicação.
3. Instalando o **Django REST framework**.

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

Logo após a criação de sua aplicação, você deverá adicioná-la ao projeto, acessando as configurações do projeto (`settings.py`) e acrescentnado em `INSTALLED_APPS`:

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

Essas aplicações já presentes são padrões do **Django**, fique a vontade para remover os que não são úteis para você.

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

