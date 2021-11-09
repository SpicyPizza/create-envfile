FROM python:3.9

WORKDIR /opt/action

COPY LICENSE README.md ./

COPY src/create-envfile.py ./create-envfile.py

ENTRYPOINT ["./opt/action/create-envfile.py"]
