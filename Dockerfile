FROM python:3.11.5

WORKDIR /home/

RUN git clone https://github.com/NAJIRAGI/leesvelog.git

WORKDIR /home/leesvelog/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-h)jabe8h@&$e+_brxeo2n_u8ly7-1$4ge(r8n(yk^zko531hxe" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]