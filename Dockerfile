FROM python:3.11.5-slim-bullseye

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]