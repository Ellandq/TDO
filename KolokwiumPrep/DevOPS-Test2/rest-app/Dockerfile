FROM node:23-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install --production

COPY . .

RUN npm test

FROM node:23-alpine
WORKDIR /app

COPY --from=builder /app ./

EXPOSE 3000

CMD ["node", "app.js"]
