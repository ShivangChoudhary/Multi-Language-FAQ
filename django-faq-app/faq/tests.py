from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
        self.assertIsNotNone(faq.question_hi)
        self.assertIsNotNone(faq.question_bn)
