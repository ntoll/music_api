from django.test import TestCase, Client
from .models import Musician, Album


class MusicianModelTests(TestCase):

    def test_create_musician(self):
        m = Musician(first_name="Nicholas", last_name="Tollervey", instrument="Tuba")
        m.save()
        result = Musician.objects.filter(first_name="Nicholas").first()
        assert result.last_name == "Tollervey"


class ViewTests(TestCase):

    def setUp(self):
        """
        Run before all other tests.
        """
        self.client = Client()

    def test_root_path(self):
        result = self.client.get("/")
        assert result.status_code == 200
        data = result.json()
        assert "users" in data
        assert "musicians" in data
        assert "albums" in data
