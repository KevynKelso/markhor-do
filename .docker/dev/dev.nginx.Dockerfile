# Start with the nginx image from docker hub
FROM nginx:alpine

LABEL maintainer="jnickerson@bscs.org" description="nginx build with media and static assets copied into the container"

# Copy all static and media files into the container
# COPY ./fieldscope_org/staticfiles ./fieldscope_org/mediafiles /

# Copy the config file into the container
COPY ./.docker/dev/dev.default.conf /etc/nginx/conf.d/default.conf
