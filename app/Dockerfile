FROM python:3.10-slim  

WORKDIR /app

# Copiar los requisitos
COPY requirements.txt /app/requirements.txt

# Actualizar pip y luego instalar las dependencias
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar el resto de la aplicación
COPY . /app/

CMD bash -c "while true; do sleep 1; done"