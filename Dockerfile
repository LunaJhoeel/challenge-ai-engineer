# Imagen base oficial
FROM python:3.9-slim

# Configura el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libffi-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia los archivos 'requirements.txt' y asegura que los paquetes estén instalados
COPY rag_service/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del directorio de trabajo en el contenedor
COPY . .

# Informa a Docker que el contenedor escucha en el puerto 8000
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

