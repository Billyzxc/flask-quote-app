FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev curl libffi-dev libpango-1.0-0 libcairo2 libpangoft2-1.0-0 libgdk-pixbuf2.0-0 fonts-liberation libnss3 libxss1 libasound2 libxcomposite1 libxrandr2 libxdamage1 libgtk-3-0 \
    && pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000"]

