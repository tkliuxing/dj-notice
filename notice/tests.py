import unittest
from django.urls import reverse
from django.test import Client
from .models import Notice
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_notice(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["content"] = "content"
    defaults["last_modify"] = "last_modify"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Notice.objects.create(**defaults)


class NoticeViewTest(unittest.TestCase):
    '''
    Tests for Notice
    '''
    def setUp(self):
        self.client = Client()

    def test_list_notice(self):
        url = reverse('app_name_notice_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_notice(self):
        url = reverse('app_name_notice_create')
        data = {
            "title": "title",
            "content": "content",
            "last_modify": "last_modify",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_notice(self):
        notice = create_notice()
        url = reverse('app_name_notice_detail', args=[notice.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_notice(self):
        notice = create_notice()
        data = {
            "title": "title",
            "content": "content",
            "last_modify": "last_modify",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('app_name_notice_update', args=[notice.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)