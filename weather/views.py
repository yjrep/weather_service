from django.http import HttpResponse


def index(request):
    return HttpResponse('index page')

def search_history(request, zip_code):
    return HttpResponse('search page')
