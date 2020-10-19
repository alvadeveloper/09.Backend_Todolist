FROM python:stretch

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-b", ":5000", "app:app"]