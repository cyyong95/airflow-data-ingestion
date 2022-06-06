#!/usr/bin/env bash
airflow db init
airflow db upgrade
airflow users create -r Admin -u admin -p admin -e test123@gmail.com -f test -l test
airflow scheduler