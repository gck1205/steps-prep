from google.cloud import bigquery

client = bigquery.Client()

project_id = "qwiklabs-gcp-01-e797a873cfa4"
dataset_id = "thelook_gcda"
table_id = "exm"
table_ref = f"{project_id}.{dataset_id}.{table_id}"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,  # Or provide a schema
)

# For a GCS file
uri = "gs://emp_1205/employees.csv"
load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)

# For a local file
# with open("your_file.csv", "rb") as source_file:
#     load_job = client.load_table_from_file(source_file, table_id, job_config=job_config)

load_job.result()  # Waits for the job to complete
print(f"Loaded {load_job.output_rows} rows into {table_id}")