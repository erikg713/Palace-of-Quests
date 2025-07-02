FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --developement
COPY . .
EXPOSE 4000
CMD ["npm", "start"]
