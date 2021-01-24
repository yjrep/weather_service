from weather.models import ZipCode
from django.shortcuts import render


def index(request):
    context = {
        'msg': 'Test message'
    }

    return render(request, 'index.html', context)

def search_history(request, zip_code):
    context = {
        'zip_code': zip_code
    }

    return render(request, 'search_result.html', context)
