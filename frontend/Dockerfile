FROM node:18 AS build

WORKDIR /app

COPY package*.json ./
RUN npm install --force
COPY . .
RUN npm run build

# Use an official Nginx image to serve the static files
FROM nginx:alpine

# Copy the static files from the previous build stage to the Nginx server's public directory
COPY --from=build /app/out /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for the web server
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]