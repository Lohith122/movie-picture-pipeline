FROM public.ecr.aws/docker/library/python:3.10-alpine
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /
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
RUN cd /app && pipenv install --system --skip-lock

COPY . /app
WORKDIR /app

USER app
EXPOSE 5000

CMD ["python", "app.py"]