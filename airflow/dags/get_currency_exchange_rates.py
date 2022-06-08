from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def hello_world(name, age):
    print(f"Hello my name is {name}. I'm {age} years old!")


with DAG(
    dag_id="get_currency_exchange_rates",
    description="This dag is to pull currency exchange rate data from various sources",
    start_date=datetime(year=2022, month=6, day=1),
    schedule_interval=None
) as dag:

    startup_op = EmptyOperator(
        task_id="startup_op",
        retries=2,
        retry_exponential_backoff=True)

    print_hello_world_in_python = PythonOperator(
        task_id="print_hello_world_in_python",
        python_callable=hello_world,
        op_kwargs={
            "name": "Ken",
            "age": 100
        })

    print_hello_world_in_bash = BashOperator(
        task_id="print_hello_world_in_bash",
        bash_command="echo \"Hello world from bash operator!!\"")

startup_op >> print_hello_world_in_python
startup_op >> print_hello_world_in_bash
