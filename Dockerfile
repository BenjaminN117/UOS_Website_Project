FROM python:latest

COPY src src

WORKDIR /src

CMD ["python", "main.py"]
EXPOSE 5000/tcp
