FROM node:10
WORKDIR /usr/src
COPY package*.json /usr/src/
RUN npm install
EXPOSE 8080/tcp
COPY * /usr/src/app/
COPY * /usr/src/
ENTRYPOINT npm run start
