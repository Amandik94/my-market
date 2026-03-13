# базовый образ
FROM python:3.11-slim

# рабочая папка
WORKDIR /app

# копируем зависимости
COPY requirements.txt .

# устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# копируем весь проект
COPY . .

# порт приложения
EXPOSE 8000

# запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]