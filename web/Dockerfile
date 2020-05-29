FROM python:3.8-slim

WORKDIR /app/src

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .
CMD ["python", "server.py"]