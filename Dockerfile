# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и проект
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Переменные среды (будет переопределено в docker-compose или .env)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Открываем порт
EXPOSE 8000

#RUN python manage.py collectstatic --noinput
# Команда по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
