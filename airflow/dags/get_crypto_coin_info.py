from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from apis.gecko import coins_get_list as coins_get_list
from apis.gecko import coins_get_by_id as coins_get_by_id

with DAG(
    dag_id="get_crypto_rates",
    description="This dag is to pull crypto price data from various sources",
    start_date=datetime(year=2022, month=6, day=1),
    schedule_interval=None
) as dag:

    start_get_coin_info = EmptyOperator(
        task_id="start_get_coin_info",
        retries=1,
        retry_exponential_backoff=True
    )

    gecko = EmptyOperator(
        task_id="gecko"
    )

    gecko_coins_get_list = PythonOperator(
        task_id="gecko_coins_get_list",
        python_callable=coins_get_list,
        retries=2,
        retry_exponential_backoff=True
    )

    gecko_coins_info_bitcoin = PythonOperator(
        task_id="gecko_coins_info_bitcoin",
        python_callable=coins_get_by_id,
        op_kwargs={
            "coin_id": "bitcoin",
        },
        retries=2,
        retry_exponential_backoff=True
    )

    gecko_coins_info_ripple = PythonOperator(
        task_id="gecko_coins_info_ripple",
        python_callable=coins_get_by_id,
        op_kwargs={
            "coin_id": "ripple",
        },
        retries=2,
        retry_exponential_backoff=True
    )

    end_get_coin_list = EmptyOperator(
        task_id="end_get_coin_list"
    )

    end_get_coin_info = EmptyOperator(
        task_id="end_get_coin_info"
    )

start_get_coin_info >> gecko
gecko >> gecko_coins_get_list >> end_get_coin_list
gecko >> gecko_coins_info_bitcoin >> end_get_coin_info
gecko >> gecko_coins_info_ripple >> end_get_coin_info


