import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import boto3  # For AWS S3 integration
import psycopg2  # For PostgreSQL integration
from io import StringIO

# Sample server log data (replace with actual log data)
data = {
    "timestamp": ["2023-10-01 12:00", "2023-10-01 12:05", "2023-10-01 12:10", "2023-10-01 12:15"],
    "server_id": ["srv1", "srv2", "srv1", "srv2"],
    "cpu_usage": [75, 60, 85, 90],
    "memory_usage": [50, 45, 55, 65],
    "status": ["ok", "ok", "high_cpu", "high_memory"]
}

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Data Analysis with Pandas and NumPy
print("Server Logs Summary:")
print(df.describe())

# Calculate average CPU and memory usage
avg_cpu = np.mean(df["cpu_usage"])
avg_memory = np.mean(df["memory_usage"])
print(f"\nAverage CPU Usage: {avg_cpu}%")
print(f"Average Memory Usage: {avg_memory}%")

# Data Visualization with Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["cpu_usage"], label="CPU Usage", marker="o")
plt.plot(df["timestamp"], df["memory_usage"], label="Memory Usage", marker="x")
plt.title("Server CPU and Memory Usage Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Usage (%)")
plt.legend()
plt.grid()
plt.show()

# Data Visualization with Plotly (Interactive)
fig = px.line(df, x="timestamp", y=["cpu_usage", "memory_usage"], title="Server Usage Over Time")
fig.show()

# Cloud Integration: Upload logs to AWS S3
def upload_to_s3(dataframe, bucket_name, file_name):
    s3 = boto3.client("s3")
    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
    print(f"Uploaded {file_name} to S3 bucket {bucket_name}")

# Replace with your S3 bucket name and file name
upload_to_s3(df, "your-s3-bucket-name", "server_logs.csv")

# Database Management: Store logs in PostgreSQL
def insert_logs_to_postgres(dataframe, table_name):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            timestamp TIMESTAMP,
            server_id VARCHAR(50),
            cpu_usage FLOAT,
            memory_usage FLOAT,
            status VARCHAR(50)
    """)
    
    # Insert data into the table
    for _, row in dataframe.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (timestamp, server_id, cpu_usage, memory_usage, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (row["timestamp"], row["server_id"], row["cpu_usage"], row["memory_usage"], row["status"]))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted logs into PostgreSQL table {table_name}")

# Replace with your table name
insert_logs_to_postgres(df, "server_logs")