FROM nginx:alpine
COPY static /usr/share/nginx/html
LABEL maintainer = "cmdsouza@docker.com"