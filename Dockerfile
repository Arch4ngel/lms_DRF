FROM python:3.12

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver 0.0.0.0:8000"]
