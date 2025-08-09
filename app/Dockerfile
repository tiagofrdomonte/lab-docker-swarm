FROM python:3.9-slim

WORKDIR /app
COPY web/requirements.txt .
RUN pip install -r requirements.txt

COPY web/ .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
