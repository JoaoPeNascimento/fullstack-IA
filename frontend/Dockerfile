FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5173

# Inicia o servidor Vite acessível fora do container
CMD ["npx", "vite", "--host", "0.0.0.0"]
