from django.test import TestCase
from .models import Quote

class QuoteModelTest(TestCase):
    def test_quote_creation(self):
        quote = Quote.objects.create(content="Testowa treść", author="Tester")
        self.assertEqual(quote.author, "Tester")
        self.assertTrue(isinstance(quote, Quote))
# Create your tests here.
