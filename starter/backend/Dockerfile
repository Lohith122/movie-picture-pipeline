FROM python:3.10-slim

WORKDIR /app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir flask flask-cors requests gunicorn

COPY . /app

EXPOSE 5000

CMD ["python", "-c", "from flask import Flask; from flask_cors import CORS; from movies.movies_api import movies_api; app = Flask(__name__); CORS(app); app.register_blueprint(movies_api); app.run(host='0.0.0.0', port=5000)"]
