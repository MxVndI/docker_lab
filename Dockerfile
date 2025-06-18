# Этап сборки
FROM python:3.10-slim as builder

WORKDIR /app

# Установка зависимостей
COPY pyproject.toml .
RUN pip install --user --no-cache-dir poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    pip install --user --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY src/ ./src/
COPY tests/ ./tests/

# Финальный этап
FROM python:3.10-alpine

WORKDIR /app

# Копируем только необходимые файлы
COPY --from=builder /root/.local/lib/python3.10/site-packages /root/.local/lib/python3.10/site-packages
COPY --from=builder /root/.local/bin /root/.local/bin
COPY --from=builder /app/src ./src

# Оптимизация размера
RUN apk --no-cache add libstdc++ && \
    find /usr/local/lib/python3.10 -type d -name "tests" -exec rm -rf {} + && \
    find /root/.local/lib/python3.10 -type d -name "__pycache__" -exec rm -rf {} + && \
    rm -rf /var/cache/apk/*

ENV PATH=/root/.local/bin:$PATH \
    PYTHONPATH=/app \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8021

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8021"]