FROM node:18
WORKDIR /backend
COPY package.json package-lock.json ./
RUN npm install
COPY . .
ENV PORT 5000
EXPOSE 5000
CMD ["node", "index.js"]
