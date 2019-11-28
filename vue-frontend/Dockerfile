FROM node:lts-alpine as builder

WORKDIR /frontend
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM node:lts-alpine as runner
COPY --from=builder /frontend/dist .
RUN npm install -g http-server

EXPOSE 8080
CMD [ "http-server", "dist" ]
