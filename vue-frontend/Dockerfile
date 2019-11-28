FROM node:lts-alpine as builder

RUN npm install -g http-server

WORKDIR /frontend

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
