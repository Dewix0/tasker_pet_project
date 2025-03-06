# Используем официальный образ Python
FROM python:3.13

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Обновляем pip и ставим зависимости
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт
EXPOSE 8000

# Команда по умолчанию при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]