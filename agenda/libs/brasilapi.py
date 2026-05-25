
from datetime import date
import requests
from django.conf import settings


def is_feriado(data: date) -> bool:
    ano = data.year

    if settings.TESTING:
        if data.day == 25 and data.month == 12:
            return True
        return False

    r = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
    if r.status_code != 200:
        raise ValueError("Nao foi possivel obter os feriados")
    feriados = r.json()
    for feriado in feriados:
        data_feriado_str = feriado['date']
        data_feriado = date.fromisoformat(data_feriado_str)
        if data == data_feriado:
            return True
    
    return False
        