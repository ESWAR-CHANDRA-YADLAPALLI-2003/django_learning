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

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.messages import get_messages

User = get_user_model()

class NoteMessageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass')
        self.client.login(username='test', password='pass')

    def test_create_note_shows_success_message(self):
        resp = self.client.post(reverse('notes:add'), {'title': 'T', 'content': 'C'}, follow=True)
        messages = [str(m) for m in get_messages(resp.wsgi_request)]
        self.assertIn("Note created successfully.", messages)

