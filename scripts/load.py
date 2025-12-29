import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO
import pandas as pd
from transform import most_bikes_station
import boto3


df = pd.DataFrame(most_bikes_station)

table = pa.Table.from_pandas(df)

buffer = BytesIO()
pq.write_table(table, buffer)
buffer.seek(0)

s3_client = boto3.client('s3')

bucket_name = 'bikeshiareairflow'

def dataframe_parquet() -> BytesIO:
    table = pa.Table.from_pandas(df)
    parquet_buffer = BytesIO()
    pq.write_table(table, parquet_buffer)
    parquet_buffer.seek(0)
    return parquet_buffer



