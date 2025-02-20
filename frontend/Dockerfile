# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app for production
RUN npm run build

# Expose port 3000 for React
EXPOSE 3000

# Serve the application using a lightweight HTTP server
CMD ["npm", "start"]
