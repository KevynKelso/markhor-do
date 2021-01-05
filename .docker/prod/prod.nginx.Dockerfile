# Start with the nginx image from docker hub
FROM nginx:alpine

LABEL maintainer="jnickerson@bscs.org" description="nginx build with media and static assets copied into the container"

# Copy the config file into the container
COPY ./.docker/prod/prod.default.conf /etc/nginx/conf.d/default.conf
