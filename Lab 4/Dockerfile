FROM alpine:latest

RUN apk add --no-cache bash shadow coreutils

RUN useradd -m may && \
    useradd -m lukasz && \
    useradd -m hajdi

ARG CONTAINER_USER=may
ENV CONTAINER_USER=${CONTAINER_USER}

COPY show_user_info.sh /home/${CONTAINER_USER}/show_user_info.sh

RUN chmod +x /home/${CONTAINER_USER}/show_user_info.sh && \
    chown ${CONTAINER_USER}:${CONTAINER_USER} /home/${CONTAINER_USER}/show_user_info.sh

USER ${CONTAINER_USER}

WORKDIR /home/${CONTAINER_USER}

CMD ["./show_user_info.sh"]
