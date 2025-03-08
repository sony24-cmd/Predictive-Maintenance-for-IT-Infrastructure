import pandas as pd
import numpy as np
import datetime

# Sample Data Generation
np.random.seed(42)
time_index = pd.date_range('2023-01-01', periods=1000, freq='H')
cpu_usage = np.random.normal(50, 10, 1000)
memory_usage = np.random.normal(60, 15, 1000)
network_traffic = np.random.normal(100, 20, 1000)
database_latency = np.random.normal(5, 1, 1000)

df = pd.DataFrame({
    'timestamp': time_index,
    'cpu_usage': cpu_usage,
    'memory_usage': memory_usage,
    'network_traffic': network_traffic,
    'database_latency': database_latency
})

# Preprocessing: Example (Add a day of week column)
df['day_of_week'] = df['timestamp'].dt.day_name()

# Output
print("Sample Preprocessed Data:")
print(df.head())

# --- Cloud Platform Examples (Conceptual) ---

# AWS (Conceptual)
def aws_data_pipeline(df, bucket_name, file_key):
    """Conceptual AWS data pipeline (S3, Glue, Athena)."""
    # 1. Store data in S3
    # s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=df.to_csv(index=False))
    print(f"AWS: Data stored in S3 bucket '{bucket_name}', key '{file_key}'.")

    # 2. AWS Glue (ETL) - Example: Run a Glue job to transform data
    # glue_client.start_job_run(JobName='my_glue_job')
    print("AWS: Glue job triggered (conceptual).")

    # 3. AWS Athena (Query) - Example: Query the data
    # athena_client.start_query_execution(QueryString='SELECT * FROM my_table', ResultConfiguration={'OutputLocation': 's3://...'})
    print("AWS: Athena query executed (conceptual).")

# Azure (Conceptual)
def azure_data_pipeline(df, container_name, file_name):
    """Conceptual Azure data pipeline (Blob Storage, Data Factory, Synapse)."""
    # 1. Store data in Blob Storage
    # blob_service_client.get_blob_client(container=container_name, blob=file_name).upload_blob(df.to_csv(index=False))
    print(f"Azure: Data stored in Blob Storage container '{container_name}', file '{file_name}'.")

    # 2. Azure Data Factory (ETL) - Example: Run a Data Factory pipeline
    # data_factory_client.create_pipeline_run(resource_group_name='...', factory_name='...', pipeline_name='...')
    print("Azure: Data Factory pipeline triggered (conceptual).")

    # 3. Azure Synapse Analytics (Query) - Example: Query the data
    # synapse_client.execute_query(workspace_name='...', sql_query='SELECT * FROM my_table')
    print("Azure: Synapse query executed (conceptual).")

# GCP (Conceptual)
def gcp_data_pipeline(df, bucket_name, blob_name):
    """Conceptual GCP data pipeline (Cloud Storage, Dataflow, BigQuery)."""
    # 1. Store data in Cloud Storage
    # bucket = storage_client.bucket(bucket_name)
    # blob = bucket.blob(blob_name)
    # blob.upload_from_string(df.to_csv(index=False))
    print(f"GCP: Data stored in Cloud Storage bucket '{bucket_name}', blob '{blob_name}'.")

    # 2. Google Cloud Dataflow (ETL) - Example: Run a Dataflow job
    # dataflow_client.projects().locations().templates().create(body={'gcsPath': 'gs://...'}, projectId='...', location='...')
    print("GCP: Dataflow job triggered (conceptual).")

    # 3. Google BigQuery (Query) - Example: Query the data
    # query_job = bigquery_client.query('SELECT * FROM my_dataset.my_table')
    print("GCP: BigQuery query executed (conceptual).")

# Example Usage (Conceptual)
aws_data_pipeline(df, 'my-monitoring-bucket', 'monitoring_data.csv')
azure_data_pipeline(df, 'monitoring-container', 'monitoring_data.csv')
gcp_data_pipeline(df, 'my-monitoring-bucket', 'monitoring_data.csv')