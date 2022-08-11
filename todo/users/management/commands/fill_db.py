from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_users = User.objects.all()
        for user in all_users:
            if user.email == 'test1@mail.ru' or user.email == 'test2@mail.ru' or user.email == 'ns_ilnur@mail.ru':
                user.delete()
        test1 = User(username='test1', first_name='test', last_name='one', email='test1@mail.ru')
        test1.save()
        test2 = User(username='test2', first_name='test', last_name='two', email='test2@mail.ru')
        test2.save()
        User.objects.create_superuser(username='Ilnur', first_name='Ильнур', last_name='Хабибрахманов',
                                      email='ns_ilnur@mail.ru', password='1')
