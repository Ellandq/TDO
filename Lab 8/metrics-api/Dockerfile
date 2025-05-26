FROM python:3.13-alpine

WORKDIR /app
COPY app.py .

RUN pip install flask
VOLUME ["/data"]
EXPOSE 80

CMD ["python", "app.py"]
