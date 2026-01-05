from datetime import datetime
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO
import pandas as pd
from etl.transform import transform_top_stations_all_networks
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def dataframe_parquet_buffer(df: pd.DataFrame) -> BytesIO:
    table = pa.Table.from_pandas(df)
    buffer = BytesIO()
    pq.write_table(table, buffer)
    buffer.seek(0)
    return buffer

def upload_to_s3(df: pd.DataFrame, bucket_name:str, s3_key:str, aws_conn_id:str = 'aws_default'):
    date_folder = datetime.utcnow().strftime('%Y-%m-%d')
    s3_key = f"bike_data/{date_folder}/{s3_key}"
    hook = S3Hook(aws_conn_id=aws_conn_id)
    buffer = dataframe_parquet_buffer(df)
    
    hook.load_file_obj(
        file_obj=buffer,
        key='bike_data/most_bikes_station.parquet',
        bucket_name='bikeshareairflow',
        replace=True
    )
    print(f"Uploaded data to s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    top_stations_df = transform_top_stations_all_networks(top_n=5)
    bucket_name = 'bikeshareairflow'
    upload_to_s3(top_stations_df, bucket_name)