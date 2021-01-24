import requests

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from requests.models import Response
from typing import Optional, Dict, Any, Tuple

from weather.forms import SearchForm
from weather.models import ZipCode, SearchResult


def weather_api_call(request: WSGIRequest) -> Dict[str, Any]:
    zip_code: ZipCode = ZipCode()
    form: SearchForm = SearchForm()
    error_msg: Optional[str] = None
    result: Optional[SearchResult] = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            result, error_msg = save_search_history(request.POST['zipcode'])

    return {
        'form': form,
        'zip_code': zip_code,
        'result': result,
        'error_msg': error_msg
    }

def save_search_history(zipcode: str) -> Tuple[Optional[SearchResult], Optional[str]]:
    error_msg: Optional[str] = None
    result: Optional[SearchResult] = None
    url: str = 'https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}&units=imperial'.format(zipcode, settings.OPENWEATHER_KEY)
    # send request to url
    resp: Response = requests.get(url)
    data: Dict[str, Any] = resp.json()

    # fetch or create zip code from ZipCode model
    zip_code, created = ZipCode.objects.get_or_create(zip_code=zipcode)
    result = SearchResult(zip_code=zip_code)
    
    if resp.status_code == 200:
        # successful request
        # update ZipCode with city name
        save_zip_code(zip_code, data)

        if 'main' in data:
            result.temperature = data['main']['temp']
            result.feels_like = data['main']['feels_like']
            result.humidity = data['main']['humidity']
            result.save()
        if 'message' in data:
            result.message = data['message']
    else:
        result.message = data['message']
        error_msg = data['message']

    # save record
    result.save()

    return result, error_msg


def save_zip_code(zip_code: ZipCode, data: Dict[str, Any]) -> None:
    try:
        zip_code.city = data['name']
        # save coords if available
        zip_code.lon = data['coord']['lon']
        zip_code.lat = data['coord']['lat']
        zip_code.save()
    except:
        pass


def weather_history(zip_code: str) -> Dict[str, Any]:
    search_results: Optional[QuerySet] = None

    try:
        search_results = ZipCode.objects.get(zip_code=zip_code).searchresult_set.all()
    except ZipCode.DoesNotExist:
        pass

    return {
        'zip_code': zip_code,
        'search_results': search_results
    }
