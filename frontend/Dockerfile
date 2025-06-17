# Stage 1: Build the React application
FROM node:18-alpine AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json (if exists) and install dependencies
COPY package.json package-lock.json ./
RUN npm install --production

# Copy the rest of the application code and build it
COPY . .
RUN npm run build

# Stage 2: Serve the React application
FROM nginx:alpine

# Copy the built React application from the previous stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
