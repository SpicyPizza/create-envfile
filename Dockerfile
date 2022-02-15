FROM python:3.10-alpine

WORKDIR /opt/action

COPY LICENSE README.md src/create-envfile.py ./

ENTRYPOINT ["./create-envfile.py"]
