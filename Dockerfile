FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONNUNBUFFERED=1

# RUN apk update && apk add --no-cache \
#     libpq-dev \
#     gcc \
#     musl-dev \
#     postgresql-dev

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
    
COPY . /app/

EXPOSE 8000

# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
