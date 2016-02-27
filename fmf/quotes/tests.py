from django.test import TestCase
from .models import Quote


class QuoteTestCase(TestCase):

    def setUp(self):
        Quote.objects.create(author="Janez Novak", content="Bla bla")

    def test_quote_str(self):
        """Quote string output test"""
        quote = Quote.objects.get(author="Janez Novak")
        self.assertEqual(quote.__str__(), "Janez Novak: Bla bla")
