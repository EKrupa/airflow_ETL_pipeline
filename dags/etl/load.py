import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO
import pandas as pd
from etl.transform import most_bikes_station
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

# Convert your transformed data to a DataFrame
df = pd.DataFrame(most_bikes_station)

def dataframe_parquet_buffer() -> BytesIO:
    """Convert DataFrame to Parquet format in a BytesIO buffer."""
    table = pa.Table.from_pandas(df)
    buffer = BytesIO()
    pq.write_table(table, buffer)
    buffer.seek(0)
    return buffer

def upload_to_s3():
    """Upload the Parquet buffer to S3 using Airflow S3Hook."""
    hook = S3Hook(aws_conn_id='bikeshare_airflow')
    buffer = dataframe_parquet_buffer()
    
    hook.load_file_obj(
        file_obj=buffer,
        key='bike_data/most_bikes_station.parquet',
        bucket_name='bikeshiareairflow',
        replace=True
    )
