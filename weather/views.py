from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http.response import HttpResponse

from weather.logic import weather_api_call, weather_history


def index(request: WSGIRequest) -> HttpResponse:
    context = weather_api_call(request)

    return render(request, 'index.html', context)

def search_history(request: WSGIRequest, zip_code: str) -> HttpResponse:
    context = weather_history(zip_code)

    return render(request, 'search_result.html', context)
