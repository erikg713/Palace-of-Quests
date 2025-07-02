FROM node:20-alpine

# Install dependencies for building native modules (optional, but often needed)
RUN apk add --no-cache python3 make g++

WORKDIR /app

# Copy only package files first for better caching
COPY package.json package-lock.json ./

# Install all dependencies, including devDependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Set development environment variable
ENV NODE_ENV=development

# Expose port, default 4000, but can be overridden at run time
ARG PORT=4000
EXPOSE $PORT

# Use nodemon for hot reload in development, fallback to npm start if not present
CMD ["npx", "nodemon", "--legacy-watch", "index.js"]

# If your main file isn't index.js adjust above accordingly
