# ---------------------------------------------------------------------------
# CarniCore backend
#
# Cambios respecto de la version anterior:
#   - node:18 -> node:22. Node 18 salio de soporte activo.
#   - `npm install --production` -> `npm ci --omit=dev`. `npm install` IGNORA
#     package-lock.json y puede instalar versiones distintas en cada build:
#     el build no era reproducible. `npm ci` lo respeta.
#   - El proceso deja de correr como root.
#   - Se anade HEALTHCHECK, para que depends_on de compose sea util.
# ---------------------------------------------------------------------------
FROM node:22-alpine

WORKDIR /usr/src/app

# Dependencias primero, para aprovechar la cache de capas de Docker.
COPY package*.json ./
RUN npm ci --omit=dev

COPY . .

ENV NODE_ENV=production
EXPOSE 4000

# node:alpine trae un usuario "node" sin privilegios. Usarlo limita el dano
# de una ejecucion de codigo arbitrario dentro del contenedor.
USER node

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD node -e "require('http').get('http://127.0.0.1:4000/health',r=>process.exit(r.statusCode===200?0:1)).on('error',()=>process.exit(1))"

CMD ["node", "src/server.js"]
