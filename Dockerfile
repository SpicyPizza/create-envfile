FROM python:3-alpine

COPY ./create-envfile.py /create-envfile.py

CMD ["python", "/create-envfile.py"]
