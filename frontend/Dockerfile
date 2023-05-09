FROM node:18.14.2-buster-slim

WORKDIR /code/frontend

COPY ./package*.json .
RUN npm install

COPY . .

WORKDIR /code/frontend
# CMD ["npm", "start"]