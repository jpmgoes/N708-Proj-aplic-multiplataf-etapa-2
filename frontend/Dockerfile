# Use a imagem base do Node.js
FROM node:18-alpine as build

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo package.json e o package-lock.json para o contêiner
COPY package*.json ./

# Instale as dependências
RUN npm install

# Copie todos os arquivos do projeto para o contêiner
COPY . .

# Compile o aplicativo React
RUN npm run build

# Use uma imagem nginx para servir o aplicativo React
FROM nginx:alpine

# Copie os arquivos compilados para o diretório padrão do nginx
COPY --from=build /app/build /usr/share/nginx/html

# Copie o arquivo de configuração do nginx (opcional, ajuste conforme necessário)
# COPY nginx.conf /etc/nginx/nginx.conf

# Exponha a porta 80 para acesso
EXPOSE 80

# Comando padrão para iniciar o nginx
CMD ["nginx", "-g", "daemon off;"]
