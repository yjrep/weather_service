import pytz

from datetime import datetime
from django import template
from typing import Optional


register = template.Library()


@register.filter
def convert_k_to_f(kelvin: Optional[float]) -> Optional[float]:
    return (kelvin * 9 / 5) - 459.67 if kelvin else None


@register.filter
def convert_timezone(time: datetime, timezone: str='US/Eastern') -> str:
    converted: str = ''

    try:
        time = time.astimezone(pytz.timezone(timezone))
        converted = time.strftime('%b %d, %Y, %I:%M:%S %p')
    except:
        pass
    
    return converted
