# review/management/commands/command_name.py

import csv
from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Genre, Review, Comment, Title, Category
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Команда заполняет базу данных'

    def handle(self, *args, **options):
        MODELS = {
            CustomUser: 'users.csv',
            Category: 'category.csv',
            Genre: 'genre.csv',
            Title: 'titles.csv',
            Review: 'review.csv',
            Comment: 'comments.csv',
        }

        try:
            for cur_model, data_file in MODELS.items():
                with open(f'{settings.BASE_DIR}\static\data\{data_file}', 'r', encoding='utf=8') as csvfile:
                    row_reader = csv.DictReader(csvfile)
                    objs = [cur_model(**data) for data in row_reader]
                    cur_model.objects.bulk_create(objs=objs, ignore_conflicts=True)

        except Exception as error:
            print(f'Остановка с ошибкой - {error} ')
        finally:
            print('Конец скрипта')
