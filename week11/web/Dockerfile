# syntax=docker/dockerfile:1
FROM python:3.8-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
WORKDIR /code/myproject
EXPOSE 8000
RUN ["python", "manage.py", "makemigrations"]
RUN ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]