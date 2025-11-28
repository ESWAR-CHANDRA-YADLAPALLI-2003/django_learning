from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from Notes_APP.models import Note

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed demo notes with demo user'

    def handle(self, *args, **kwargs):
        u, created = User.objects.get_or_create(username='demo', defaults={'email':'demo@example.com'})
        if created:
            u.set_password('demo123')
            u.save()
        else:
            u.set_password('demo123')
            u.save()

        if not Note.objects.filter(owner=u).exists():
            for i in range(1, 11):
                Note.objects.create(
                    title=f'Demo Note {i}',
                    description='This is a sample note created for demo purposes. ' + str(i),
                    owner=u
                )
        self.stdout.write(self.style.SUCCESS('Seeded demo notes (demo / demo123)'))
