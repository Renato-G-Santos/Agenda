FROM python:3.14.4-slim

WORKDIR /app

COPY requirements/ /app/

RUN python -m pip install --no-cache-dir -r dev.txt

COPY . .


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
