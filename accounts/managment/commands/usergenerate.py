from django.core.management.base import BaseCommand
from accounts.models import Account


# Command for create superuser
class Command(BaseCommand):
    help = 'Create superuser'  # help for command

    def handle(self, *args, **options):  # handle command
        username = 'erlan'  # username
        email = 'era.ab.02@gmail.com'  # email
        password = '123321era'  # password
        reset_key = '123321era'  # reset key
        user = Account.objects.create_superuser(
            username=username,
            email=email,
            reset_password_key=reset_key,
            password=password
        )  # create superuser
        user.save()  # save superuser
        print('Superuser created')  # print message
