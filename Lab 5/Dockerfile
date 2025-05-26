ARG NODE_VERSION=18

# FRONT BUILD STAGE
FROM node:${NODE_VERSION}-alpine AS frontend-builder
WORKDIR /frontend

# Dependencies for the front
COPY frontend/package*json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# BACKEND BASE STAGE
FROM node:${NODE_VERSION}-alpine AS backend-base
WORKDIR /backend

ONBUILD COPY backend/package*.json ./
ONBUILD RUN npm ci --only=products

# BACKEND PREP STAGE
FROM backend-base AS backend-prepared
COPY backend/ ./

# FINAL STAGE
FROM node:${NODE_VERSION}-alpine AS final
WORKDIR /app

# Env prep
ENV NODE_ENV=production
ENV PORT=3000

COPY --from=backend-prepared /backend /app
COPY --from=frontend-builder /frontend/build /app/public

EXPOSE 3000

CMD ["node", "server.js"]