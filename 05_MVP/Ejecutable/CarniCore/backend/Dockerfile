FROM node:18-alpine

WORKDIR /usr/src/app

# Instala dependencias primero para aprovechar la caché de Docker
COPY package*.json ./
RUN npm install --production

# Copia el resto del código fuente
COPY . .

ENV NODE_ENV=production
EXPOSE 4000

CMD ["node", "src/server.js"]
