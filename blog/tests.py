from django.test import TestCase
from blog.models import Entry

# Create your tests here.

class EntryModelTest(TestCase):

    def setUp(self):
        self.entry = Entry(title="entry title")

    def test_string_representation(self):
        self.assertEqual(str(self.entry), self.entry.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)