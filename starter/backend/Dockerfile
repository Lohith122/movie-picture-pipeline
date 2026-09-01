FROM public.ecr.aws/docker/library/python:3.10-alpine

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
RUN cd /app && pipenv install --system --deploy --ignore-pipfile || pipenv install --skip-lock

COPY . /app

USER app
EXPOSE 5000

CMD ["pipenv", "run", "movie"]
