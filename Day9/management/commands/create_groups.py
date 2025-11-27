# Day9/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Create initial groups and assign permissions'

    def handle(self, *args, **options):
        Task = apps.get_model('Day9', 'Task')
        perms = Permission.objects.filter(content_type__app_label='Day9')
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        editor_group, _ = Group.objects.get_or_create(name='Editor')
        viewer_group, _ = Group.objects.get_or_create(name='Viewer')

        # Admin -> all Day9 perms
        admin_group.permissions.set(perms)

        # Editor -> add/change/view
        editor_perms = perms.filter(codename__in=['add_task','change_task','view_task'])
        editor_group.permissions.set(editor_perms)

        # Viewer -> view only
        view_perm = perms.filter(codename='view_task')
        viewer_group.permissions.set(view_perm)

        self.stdout.write(self.style.SUCCESS('Groups created/updated.'))
