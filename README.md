### Инструкция

## Технологии
Python 3.12
Django 5.0
Django Rest Framework 3.15
## Клонирование проекта
```
git clone https://github.com/TheSweetieTea/foods.git
```
## Создание виртуального окружения
```
python3 -m venv venv 
```
## Активация виртуального окружения Mac/Linux
```
source venv/bin/activate
```
## Скопируйте и настройте значения переменных окружения
```
cp .env.example .env
```
## Установка зависимостей
```
pip3 install -r requirements.txt
``` 
## Миграции
- Создание миграциий
```
python3 manage.py makemigrations
```
- Применение миграции
```
python3 manage.py migrate
```
## Запуск проекта в dev-режиме
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```