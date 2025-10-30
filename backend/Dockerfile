# Etapa base — imagem leve do Python
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Evita criação de cache e arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Copia os arquivos de dependência
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando padrão (utilizando uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
