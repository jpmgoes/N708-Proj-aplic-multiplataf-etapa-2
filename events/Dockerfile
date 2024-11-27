# Usar imagem base Python
FROM python:3.10-slim

# Configurar diretório de trabalho
WORKDIR /app

# Copiar dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do serviço
COPY . .

# Comando para iniciar o serviço
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
