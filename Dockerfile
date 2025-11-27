# Dockerfile - Mayte Anahi Anchapanta Vinueza
FROM python:3.10-slim

WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY test_app.py .

# Exponer puerto
EXPOSE 1004

# Etiquetas
LABEL maintainer="Mayte Anahi Anchapanta Vinueza"
LABEL version="vinueza-1.0.5"

# Comando de inicio
CMD ["python", "app.py"]