from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from kafka_producer import fetch_and_publish_news

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="news_api_pipeline",
    default_args=default_args,
    description="Fetch news from API and stream via Kafka",
    schedule_interval="@hourly",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="fetch_news",
        python_callable=fetch_and_publish_news,
    )

    task1
