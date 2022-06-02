FROM python:3.9.12

WORKDIR app

COPY requirements.txt ./
COPY .env ./

RUN pip3 install -r requirements.txt

COPY src src

ENTRYPOINT ["python", "src/main.py"]