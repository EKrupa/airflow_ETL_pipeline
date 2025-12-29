from airflow import DAG, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.bash import BashOperator

from datetime import datetime

from scripts.load import dataframe_parquet

with DAG(
    dag_id='bike_etl_dag',
    start_date=datetime(2025, 12, 6),
    schedule_interval='*/15 * * * *', #run every 15 minutes
    catchup=False, #set to False to avoid backfilling
    tags=['bike'],
) as dag:
    task_one = BashOperator(
        task_id='print_current_time',
        bash_command='echo "Hello Evan"',
        dag=dag,

    )

    task_two = BashOperator(
        task_id='list_bike_data_files',
        bash_command='echo "Current time is: $(date)"'

    )
    task_one >> task_two