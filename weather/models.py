from django.db import models


class ZipCode(models.Model):
    zip_code = models.CharField(max_length=5, unique=True, blank=False, null=False)
    city = models.CharField(max_length=255, default=None, blank=True, null=True)
    lon = models.FloatField(default=None, blank=True, null=True)
    lat = models.FloatField(default=None, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if self.city:
            return '{} ({})'.format(self.zip_code, self.city)
        return self.zip_code


class SearchResult(models.Model):
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    temperature = models.FloatField(default=None, blank=True, null=True)
    feels_like = models.FloatField(default=None, blank=True, null=True)
    humidity = models.IntegerField(default=None, blank=True, null=True)
    message = models.CharField(max_length=255, default=None, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.zip_code.zip_code
