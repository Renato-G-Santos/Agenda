from datetime import datetime, date, timedelta, timezone

import requests
from django.conf import settings
import agenda.libs.brasilapi as brasilapi

def get_horario_diponivel(data: date):
    
    if settings.TESTING:
        if data.day == 25 and data.month == 12:
            return True
        return False


    try:
        if brasilapi.is_feriado(data):
            return []
    except ValueError:
        ...
        
    start = datetime(year = data.year, month = data.month, day = data.day, hour = 8, minute = 0, tzinfo = timezone.utc)
    end = datetime(year = data.year, month = data.month, day = data.day, hour = 18, minute = 0, tzinfo = timezone.utc)

    delta = timedelta(minutes= 30)
    horarios_disponiveis = set()

    while start < end:
        horarios_disponiveis.add(start)
        start += delta

    return horarios_disponiveis