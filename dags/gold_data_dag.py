import sys
from datetime import datetime, timedelta
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
sys.path.append('/opt/airflow')
from src.config import GOLD_API_URL
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

default_args = {
    'owner': 'Dung',
    'depends_on_past': False,
    'email': ['phamthanhdung1112@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='gold_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline: Extract → Transform → Load gold price data',
    schedule='@daily',
    start_date=datetime(2025, 10, 11),
    catchup=False,
    tags=['etl', 'gold'],
) as dag:

    def run_extract(**context):
        run_date = context['ds'].replace('-', '')
        run_date = int(run_date) - 1
        run_date = str(run_date)
        print(f"Fetching gold data for date: {run_date}")
        df = extract_data(run_date)
        print(df)
        context['ti'].xcom_push(key='raw_data', value=df.to_json())

    def run_transform(**context):
        raw_json = context['ti'].xcom_pull(task_ids='extract_task', key='raw_data')
        df_raw = pd.read_json(raw_json)
        df_transformed = transform_data(df_raw)
        context['ti'].xcom_push(key='transformed_data', value=df_transformed.to_json())

    def run_load(**context):
        transformed_json = context['ti'].xcom_pull(task_ids='transform_task', key='transformed_data')
        df = pd.read_json(transformed_json)
        date_str = context['ds'].replace('-', '')
        date_str = int(date_str) - 1
        date_str = str(date_str)
        load_data(df, date_str)
        print(f"Data for {date_str} sent successfully by email.")


    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=run_extract,
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=run_transform,
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=run_load,
    )

    extract_task >> transform_task >> load_task
