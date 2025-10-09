Emp	Dept	Salary
1	1	300
2	1	500
3	1	500
4	1	700
5	2	100
6	2	300
7	2	400
8	3	200
9	3	400
10	3	600

with 
(select emp,dept,dense_rank() over ( group by dept order by sal) as rn from emp)
select * f
===============================
authenticate to cloud storage using service account - python code
authenticate to cloud storage using service account - cli
pyspark code to read data from csv file in cloud storage
======================
INFORMATION_SCHEMA.JOBS_BY_ORGANIZATION: Provides near real-time metadata for all jobs submitted within the entire organization.
INFORMATION_SCHEMA.JOBS_BY_FOLDER: Offers a consolidated view of jobs executed from projects within a specified parent folder. 
INFORMATION_SCHEMA.JOBS_BY_PROJECT: Displays job-level data for a specific project.
INFORMATION_SCHEMA.JOBS_BY_USER: Shows jobs submitted by a particular user.
===================================

===================

import pyspark
from pyspark.sql import SparkSession


spark=SparkSession
     .create.
	 
df=spark.read("").options(header=True).inferschema(True)

df.write().


==============

This payment method can’t be used for recurring payments. Learn more [OR-ACH-01]

This payment method can’t be used for recurring payments. Learn more [OR-ACH-01]
=========================

select * from qwiklabs-gcp-01-f56093fc4d92.`region-us`.INFORMATION_SCHEMA.TABLE_STORAGE

select * from `qwiklabs-gcp-01-f56093fc4d92.bq_logs.INFORMATION_SCHEMA.TABLES`

===========================
Minimizing I/O -- select required columns instead of *
Caching results of previous queries:
   The BigQuery service automatically caches query results in a temporary table. 
   If the identical query is submitted within approximately 24 hours, the results are served from this temporary table without any recomputation.
   Cached results are extremely fast and do not incur charges.
   --Accelerate queries with BI Engine
Performing efficient joins --> 
Avoid overwhelming single workers --> row_number( partition by over by)
Using approximate aggregation functions : APPROX_COUNT_DISTINCT --> faster than count(distinct)

====================
WITH
  Sequences AS (
    SELECT [0, 1, 1, 2, 3, 5] AS some_numbers 
    UNION ALL
    SELECT [2, 4, 8, 16, 32] 
    UNION ALL
    SELECT [5, 10]
  )
SELECT some_numbers,some_numbers[0],some_numbers[OFFSET(1)],some_numbers[ORDINAL(2)]
FROM Sequences s;
====================================

Airflow:

default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2023,11,1),
  'email': ['airflowresults@datacamp.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}


from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

External providers
from airflow.providers.http.operators.http import SimpleHttpOperator

Sensor:
from airflow.sensors.filesystem import FileSensor


SLA
within airflow,the amount of time a task or a DAG should require to run
sla - argument on the task

default_args = {
  'start_date': datetime(2024, 1, 20),
  'sla': timedelta(minutes=30)
}

Templates:
Allow substitution info. during a dag run
are created using jinja template format
#########

API Pagination:
Normalization/DeNormalization:

Clustered by/Partition by:

PII tagging:

IAM roles:
####
Dataflow & Dataproc:
Service Model: Dataflow is serverless, while Dataproc involves managing clusters. 
Programming Model: Dataflow uses Apache Beam for portable pipelines, whereas Dataproc runs jobs on traditional Hadoop/Spark clusters. 
Scalability: Dataflow provides automatic scaling, while Dataproc requires manual cluster scaling. 
Hadoop Dependence: Choose Dataproc if your application has existing dependencies on the Hadoop ecosystem; Dataflow abstracts away this dependency. 


XML & json files:

rdd
df --> to hive

json files:

dataproc airflow operators:

optimization techniques:

BQ vs SQL:

onprem --> connectdirect jobs -->hive --> bq

Cloud Run:

