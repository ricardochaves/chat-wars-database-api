from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


def add_user():
    if not User.objects.filter(username="admin").exists():
        u = User(username="admin")
        u.set_password("test")
        u.is_superuser = True
        u.is_staff = True
        u.save()


class Command(BaseCommand):
    help = "Create a super user"

    def handle(self, *args, **options):
        add_user()
