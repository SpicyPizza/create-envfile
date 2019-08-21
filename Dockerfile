FROM alpine:3.10

COPY LICENSE README.md src/create-envfile.py entrypoint.sh /

RUN apk add python3

ENTRYPOINT ["/entrypoint.sh"]

