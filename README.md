# api_yamdb

![Logo](https://cdn-irec.r-99.com/sites/default/files/product-images/399872/EOXOqQkXnjTMTRnIpMUSvQ.jpg)

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти из пользовательских оценок формируется рейтинг (целое число). 

Настройка и запуск сервера:
Cоздать и активировать виртуальное окружение:
_python -m venv venv_
_Source venv/Scripts/activate_
Установить зависимости из файла requirements.txt:
_pip install -r requirements.txt_	
Перейти в основную папку и выполнить миграции:
_cd api_yamdb_
Выполнить миграцию:
_python manage.py migrate_
Запустить проект:
_python manage.py runserver_
ЗАВИСИМОСТИ:
_Request==2.26.0
Django==2.2.16
Djangorestframework==3.12.4
PyJWT==2.1.0
Pytest==6.2.4
Pytest-django==4.4.0
Pytest-pythonpath==0.7.3
Django-filter==2.2.0
Djangorestframework-simplejwt=5.2.0_
ТЕХНОЛОГИИ:
_Python 3.8
Django 2.2.16
Djangorestframework 3.12.4
Redoc_

## Authors

- [Yana Bubnova](https://github.com/Kasaress)
- [@p1rt-py](https://github.com/p1rt-py)
