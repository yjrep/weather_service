from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<zip_code>\d{5})/$', views.search_history, name='history')
]
