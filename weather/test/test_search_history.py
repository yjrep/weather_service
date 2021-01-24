from django.test import TestCase
from random import randrange

from weather.logic import weather_history, PER_PAGE
from weather.models import ZipCode, SearchResult


class SearchResultTestCase(TestCase):
    def setUp(self) -> None:
        self.zip_code = ZipCode.objects.create(zip_code="11111", city="City A")

        for _ in range(PER_PAGE * 2):
            temp = randrange(10000) / 100
            SearchResult.objects.create(
                zip_code=self.zip_code,
                temperature=temp,
                feels_like=temp - randrange(10),
                humidity=randrange(100)
            )

    def test_search_history_created(self) -> None:
        self.assertEqual(self.zip_code.searchresult_set.all().count(), 10)

    def test_search_history(self) -> None:
        context = weather_history(self.zip_code.zip_code, 1)
        
        self.assertTrue(context['search_results'].has_other_pages)
        self.assertEqual(context['search_results'].number, 1)
        self.assertEqual(len(context['search_results']), PER_PAGE)
        