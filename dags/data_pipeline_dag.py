from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys

# Add the scripts directory to PYTHONPATH
sys.path.append(os.path.abspath("/scripts"))

from load_remote_csv import load_remote_csv
from process_with_pandas_and_spark import process_with_pandas_and_spark
from spark_streaming_1 import spark_streaming_1
from python_data_generator import python_data_generator
from publish_to_kafka import publish_to_kafka
from spark_streaming_2 import spark_streaming_2
from store_to_minio import store_to_minio
from index_to_elasticsearch import index_to_elasticsearch

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['mysol.c.t@gmail.com'],  # Replace with your email
    'email_on_failure': True,  # Send email on failure
    'email_on_retry': False,
    'retries': 3,  # Retry 3 times on failure
    'retry_delay': timedelta(minutes=5),  # 5-minute delay between retries
}

# Define the DAG
with DAG(
    'data_pipeline_dag',
    default_args=default_args,
    description='A data processing pipeline orchestrated by Airflow',
    schedule_interval='@hourly',  # Run every hour
    start_date=datetime(2025, 4, 25),
    catchup=False,
) as dag:
    
    # Task 1: Download remote CSV
    t1 = PythonOperator(
        task_id='load_remote_csv',
        python_callable=load_remote_csv
    )
    
    # Task 2: Process with Pandas and Spark
    t2 = PythonOperator(
        task_id='process_with_pandas_and_spark',
        python_callable=process_with_pandas_and_spark
    )
    
    # Task 3: Stream CSV with Spark Streaming
    t3 = PythonOperator(
        task_id='spark_streaming_1',
        python_callable=spark_streaming_1
    )
    
    # Task 4: Generate additional data
    t4 = PythonOperator(
        task_id='python_data_generator',
        python_callable=python_data_generator
    )
    
    # Task 5: Publish data to Kafka
    t5 = PythonOperator(
        task_id='publish_to_kafka',
        python_callable=publish_to_kafka
    )
    
    # Task 6: Consume Kafka data with Spark Streaming
    t6 = PythonOperator(
        task_id='spark_streaming_2',
        python_callable=spark_streaming_2
    )
    
    # Task 7: Store data in MinIO
    t7 = PythonOperator(
        task_id='store_to_minio',
        python_callable=store_to_minio
    )
    
    # Task 8: Index data in Elasticsearch
    t8 = PythonOperator(
        task_id='index_to_elasticsearch',
        python_callable=index_to_elasticsearch
    )
    
    # Define task dependencies
    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8