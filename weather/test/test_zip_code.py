from django.test import TestCase

from weather.models import ZipCode


class ZipCodeTestCase(TestCase):
    def setUp(self) -> None:
        ZipCode.objects.create(zip_code="11111", city="City A")
        ZipCode.objects.create(zip_code="22222", city="City B")

    def test_zipcode_record_created(self) -> None:
        zipcodes = ZipCode.objects.all()

        self.assertEqual(zipcodes.count(), 2)
        