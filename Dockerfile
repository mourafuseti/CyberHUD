FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Fixamos a versão 0.10.9 que é muito estável
RUN pip install --no-cache-dir opencv-python mediapipe==0.10.9

WORKDIR /app
# Copiamos com um nome diferente para garantir que o Docker não use cache antigo
COPY main.py ./cyber_main.py

CMD ["python", "cyber_main.py"]