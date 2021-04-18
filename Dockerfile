FROM python:3-alpine

COPY . .

CMD ["python", "./create-envfile.py"]
