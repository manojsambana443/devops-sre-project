FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd --system appgroup \
    && useradd --system --gid appgroup --no-create-home appuser

ARG APP_SOURCE=app
COPY --chown=appuser:appgroup ${APP_SOURCE}/ /app/

USER appuser:appgroup

EXPOSE 8080

CMD ["python", "-u", "app.py"]
