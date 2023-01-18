import random

from django.core.management.base import BaseCommand
from account.models import CustomUser, Gender


class Command(BaseCommand):
    help = 'Создание суперпользователя'

    def handle(self, *args, **options):
        if not CustomUser.objects.count():  # Если пользователей нет в БД

            gender = Gender.objects.create(
                name=random.choice(['м', 'ж'])
            )  # Создаем пол "мужской"
            # Создаем суперпользователя
            CustomUser.objects.create_superuser(
                username='admin',
                password='admin',

                first_name='admin',
                last_name='admin',
                # выбираем пол из списка
                secret='admin',
                gender=gender
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь создан'))
        else:
            self.stdout.write(self.style.WARNING('Суперпользователь уже существует'))

# Path: account\management\commands\create_superuser.py
