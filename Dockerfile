FROM python:stretch

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN source venv/bin/activate
CMD ["gunicorn", "-b", ":8080", "app:create_app("app")"]