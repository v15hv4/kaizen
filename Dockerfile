FROM python:3.8.13-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD python -m bot
