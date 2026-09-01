FROM public.ecr.aws/docker/library/python:3.10-alpine

ENV FLASK_APP=movies:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser -u 1000 -D app

RUN apk update && \
    apk add \
    pcre \
    pcre-dev \
    build-base \
    gcc \
    linux-headers \
    openssl \
    libffi-dev \
    && pip install pipenv

COPY Pipfile* /app/
RUN cd /app && pipenv install --system --skip-lock || pip install Flask gunicorn flask-cors requests

COPY . /app

USER app
EXPOSE 5000

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:5000 'movies:app' || python -m flask run --host=0.0.0.0 --port=5000 || python movies/__init__.py"]
