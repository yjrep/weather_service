from weather.models import ZipCode
from django.shortcuts import render

from .forms import SearchForm


def index(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
    

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)

def search_history(request, zip_code):
    context = {
        'zip_code': zip_code
    }

    return render(request, 'search_result.html', context)
