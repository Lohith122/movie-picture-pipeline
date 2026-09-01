FROM python:3.10-slim

WORKDIR /app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir pipenv gunicorn flask flask-cors requests

COPY Pipfile* ./
RUN pipenv install --system --skip-lock || true

COPY . .

EXPOSE 5000

CMD ["python", "-m", "movies"]
