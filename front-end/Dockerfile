FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /frontend
COPY . .
RUN npm install && \
    npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]