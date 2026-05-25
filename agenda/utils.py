from datetime import datetime, date, timedelta, timezone

import requests
import agenda.libs.brasilapi as brasilapi

def get_horario_diponivel(data: date):

    if brasilapi.is_feriado(data):
        return []
        
    start = datetime(year = data.year, month = data.month, day = data.day, hour = 8, minute = 0, tzinfo = timezone.utc)
    end = datetime(year = data.year, month = data.month, day = data.day, hour = 18, minute = 0, tzinfo = timezone.utc)

    delta = timedelta(minutes= 30)
    horarios_disponiveis = set()

    while start < end:
        horarios_disponiveis.add(start)
        start += delta

    return horarios_disponiveis