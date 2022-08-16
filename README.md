# api_yamdb

![Logo](https://cdn-irec.r-99.com/sites/default/files/product-images/399872/EOXOqQkXnjTMTRnIpMUSvQ.jpg)

The YaMDb project collects reviews (Review) of users on works (Titles).\
The works are divided into categories: "Books", "Films", "Music".\
The works themselves are not stored in YaMDb; you cannot watch a movie or listen to music here.\
There are works in each category: books, films or music.\
A work can be assigned a genre (Genre) from the list of preset ones (for example, "Fairy Tale", "Rock" or "Arthouse"). New genres can only be created by the administrator.\
Grateful or indignant users leave text reviews (Review) for the works and rate the product in the range from one to ten; a rating (integer) is formed from the user ratings.

**SETTING UP AND STARTING THE SERVER:**\
**Create and activate virtual environment:**\
_python -m venv venv_ \
_source venv/Scripts/activate_

**Install dependencies from a file requirements.txt:**\
_python -m pip install --upgrade pip_
_pip install -r requirements.txt_

**Go to main folder and run migrations:**\
_cd api_yamdb_

**Run Migration:**\
_python manage.py makemigrations_
_python manage.py migrate_
_py manage.py createsuperuser_

**Start project:**\
_python manage.py runserver_

**DEPENDENCIES:**\
_Request==2.26.0
Django==2.2.16
Djangorestframework==3.12.4
PyJWT==2.1.0
Pytest==6.2.4\
Pytest-django==4.4.0
Pytest-pythonpath==0.7.3
Django-filter==2.2.0
Djangorestframework-simplejwt=5.2.0_

**API DOC**
<http://127.0.0.1:8000/redoc/>

**TECHNOLOGY:**
_Python 3.8
Django 2.2.16
Djangorestframework 3.12.4
Redoc_

## Authors

- [Yana Bubnova](https://github.com/Kasaress)
- [@p1rt-py](https://github.com/p1rt-py)