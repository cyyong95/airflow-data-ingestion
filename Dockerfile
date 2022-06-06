FROM apache/airflow:slim-latest-python3.9

USER root

COPY ./airflow/scripts/entrypoint.sh ./entrypoint.sh
COPY ./airflow/scripts/webserver.sh ./webserver.sh

RUN chmod +x ./entrypoint.sh
RUN chmod +x ./webserver.sh

USER airflow

COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt