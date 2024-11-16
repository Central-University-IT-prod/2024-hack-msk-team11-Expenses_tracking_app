# Используем Python 3.11
FROM python:3.11

WORKDIR /backend

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src backend/src
COPY run.sh .

# Экспонируем порт для FastAPI
EXPOSE 8000

# Делаем скрипт исполняемым
RUN chmod +x ./run.sh

# Запускаем скрипт
CMD ["./run.sh"]
