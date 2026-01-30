FROM python:3.13.7

RUN pip install gunicorn==23.0.0

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:80", "hitalentapi.wsgi"]