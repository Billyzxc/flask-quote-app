# 使用官方 Python 映像檔
FROM python:3.10-slim

# 設定環境變數
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安裝系統相依套件
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev curl libffi-dev libpango-1.0-0 libcairo2 libpangoft2-1.0-0 libgdk-pixbuf2.0-0 fonts-liberation libnss3 libxss1 libasound2 libxcomposite1 libxrandr2 libxdamage1 libgtk-3-0 \
    && pip install --upgrade pip

# 建立應用目錄
WORKDIR /app

# 複製依賴與程式碼
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# 使用 gunicorn 啟動 Flask 應用
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000"]

