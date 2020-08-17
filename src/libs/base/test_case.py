from django.test import TestCase


class BaseTestCase(TestCase):
    databases = '__all__'
