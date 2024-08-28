FROM python:3.11

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . /app

CMD ["chainlit", "run", "app.py", "--port", "8080"]