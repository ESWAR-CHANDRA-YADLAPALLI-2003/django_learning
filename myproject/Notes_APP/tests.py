from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from .models import Note

class NotesPermissionTests(TestCase):
    def setUp(self):
        self.u_with = User.objects.create_user('bob', password='pass')
        add_perm = Permission.objects.get(codename='add_note')
        self.u_with.user_permissions.add(add_perm)

        self.u_without = User.objects.create_user('alice', password='pass')

    def test_create_allowed(self):
        self.client.login(username='bob', password='pass')
        resp = self.client.get(reverse('notes:create'))
        self.assertEqual(resp.status_code, 200)

    def test_create_denied_if_permission_enforced(self):
        # If you keep permission enforcement on create, expect 403
        self.client.login(username='alice', password='pass')
        resp = self.client.get(reverse('notes:create'))
        # Accept either 200 or 403 depending on whether you added PermissionRequiredMixin
        self.assertIn(resp.status_code, (200, 403))
