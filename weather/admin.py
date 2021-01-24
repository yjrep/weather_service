from django.contrib import admin

from weather.models import ZipCode, SearchResult


class ZipCodeAdmin(admin.ModelAdmin):
    pass


class SearchResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(ZipCode, ZipCodeAdmin)
admin.site.register(SearchResult, SearchResultAdmin)
