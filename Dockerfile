FROM python:3.11.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/home/demouser/.local/bin:$PATH"

RUN adduser --disabled-password --no-create-home demouser

WORKDIR /app

COPY . .

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

USER demouser
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:8000/health/ || exit 1

EXPOSE 8000

CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8000"]