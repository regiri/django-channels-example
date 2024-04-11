# django-channels example
Простой пример написанный по документации django-channels, написанный чтобы понять как работать с WebSockets в Django
# Инструкция по запуску проекта в dev-режиме
## Установка виртуального окружения
```sh
python -m venv venv
```
## Активация виртуального окружения
### Windows
```sh
venv\Scripts\activate
```
### Linux
```sh
source venv/Scripts/activate
```
## Установка зависимостей для работы с проектом
```sh
pip install -r req.txt
```
## Создание миграций и их применение:
```sh
python manage.py makemigrations
python manage.py migrate
```
## Запуск проекта в dev-режиме
```sh
python manage.py runserver
```