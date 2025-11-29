# Day9/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission
from .models import Task

class PermissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # User with permission
        self.user_allowed = User.objects.create_user('bob', password='pass')
        add_task_perm = Permission.objects.get(codename='add_task')
        self.user_allowed.user_permissions.add(add_task_perm)
        
        # User without permission
        self.user_denied = User.objects.create_user('alice', password='pass')

    def test_create_task_view_allowed(self):
        # Login user with permission
        self.client.login(username='bob', password='pass')
        resp = self.client.get('/Day9/tasks/create/')
        self.assertEqual(resp.status_code, 200)  # Allowed user should get 200

    def test_create_task_view_denied(self):
        # Login user without permission
        self.client.login(username='alice', password='pass')
        resp = self.client.get('/Day9/tasks/create/')
        self.assertEqual(resp.status_code, 403)  # Denied user should get 403
