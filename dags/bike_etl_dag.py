from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd
from etl.load import upload_to_s3

from datetime import datetime





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
        

    )

    task_two = BashOperator(
        task_id='list_bike_data_files',
        bash_command='echo "Current time is: $(date)"'

    )

    def run_bike_etl():
        from etl.transform import transform_top_stations_all_networks
        from etl.load import upload_to_s3

        df = transform_top_stations_all_networks(top_n=5)
        bucket_name = 'bikeshareairflow'
        upload_to_s3(df, bucket_name=bucket_name)


    

    run_etl_task = PythonOperator(
        task_id='run_bike_etl',
        python_callable=run_bike_etl
    )