FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы из текущего каталога внутрь контейнера
COPY . /app

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Команда, которая будет выполнена при запуске контейнера
CMD ["python", "service_exchange.py"]