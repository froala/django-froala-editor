FROM python:2

WORKDIR /usr/src/app
COPY . .
RUN pip install django
RUN pip install wand
EXPOSE 8000
WORKDIR django_examples/
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
