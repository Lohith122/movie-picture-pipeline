FROM python:3.10-slim

WORKDIR /app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir flask flask-cors requests gunicorn

COPY . /app

EXPOSE 5000

CMD ["python", "-c", "from flask import Flask; from flask_cors import CORS; from movies.resources import Movies; app = Flask(__name__); CORS(app); view = Movies.as_view('movies'); app.add_url_rule('/movies/movies', defaults={'movie_id': None}, view_func=view, methods=['GET', 'POST']); app.add_url_rule('/movies', defaults={'movie_id': None}, view_func=view, methods=['GET', 'POST']); app.add_url_rule('/', defaults={'movie_id': None}, view_func=view, methods=['GET', 'POST']); app.run(host='0.0.0.0', port=5000)"]
