FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN python -m pip install -r dev.txt


EXPOSE 8000

CMD ["python" "manage.py" "runserver" "0.0.0.0:8000"]
