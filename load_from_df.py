from google.cloud import bigquery
import pandas as pd

# Initialize BigQuery client
client = bigquery.Client()

# Define your project, dataset, and table
project_id = "qwiklabs-gcp-01-e797a873cfa4"
dataset_id = "thelook_gcda"
table_id = "emp"
table_ref = f"{project_id}.{dataset_id}.{table_id}"

# Create a sample DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 24, 35]}
df = pd.DataFrame(data)

# Configure the load job
job_config = bigquery.LoadJobConfig(
    # Specify schema if you want to explicitly define data types
    # schema=[
    #     bigquery.SchemaField("name", bigquery.enums.SqlTypeNames.STRING),
    #     bigquery.SchemaField("age", bigquery.enums.SqlTypeNames.INTEGER),
    # ],
    # # Overwrite the table or append data
    write_disposition="WRITE_TRUNCATE",  # or "WRITE_APPEND"
    create_disposition="CREATE_IF_NEEDED"
)

# Load data from DataFrame to BigQuery
job = client.load_table_from_dataframe(
    df, table_ref, job_config=job_config
)

# Wait for the job to complete
job.result()

print(f"Loaded {job.output_rows} rows into {table_ref}")