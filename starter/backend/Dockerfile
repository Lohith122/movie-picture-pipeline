FROM python:3.10-slim

WORKDIR /app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir gunicorn flask flask-cors requests pipenv

COPY Pipfile* setup.py* ./
RUN pipenv install --system --skip-lock || true

COPY . .

RUN pip install --no-cache-dir -e . || pip install --no-cache-dir . || true

EXPOSE 5000

CMD ["python", "-c", "import movies; app = getattr(movies, 'app', getattr(movies, 'application', getattr(movies, 'api', None))); hasattr(movies, 'main') and movies.main() if not app else app.run(host='0.0.0.0', port=5000)"]
