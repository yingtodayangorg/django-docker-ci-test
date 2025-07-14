FROM python:3.11.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/home/demouser/.local/bin:$PATH"

RUN addgroup --system demogroup && adduser --system --ingroup demogroup demouser

WORKDIR /app
RUN mkdir -p /app && chown -R demouser:demogroup /app



COPY --chown=demouser:demogroup requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY --chown=demouser:demogroup . .

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:8000/health/ || exit 1

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER demouser
ENTRYPOINT ["/entrypoint.sh"]