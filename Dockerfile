FROM python:3.9-slim

RUN apt update
RUN apt install -y python3-pip
RUN apt clean
RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

WORKDIR /app

EXPOSE 8005

COPY . .

CMD ["waitress-serve", "--host=0.0.0.0", "--port=8005", "app:app"]
