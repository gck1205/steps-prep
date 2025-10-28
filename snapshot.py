################
EXPORT DATA OPTIONS(
  uri='gs://my_bucket/snapshot_export_*.parquet',
  format='PARQUET',
  overwrite=true
) AS (
  SELECT * FROM `my_project.my_dataset.my_table_snapshot`
);

################
bq extract \
--compression=GZIP \
--destination_format=CSV \
my_project:my_dataset.my_table_snapshot \
gs://my_bucket/my_data/snapshot_export_*.csv.gz

###########create snapshot table

CREATE SNAPSHOT TABLE SNAPSHOT_PROJECT_ID.SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME
CLONE TABLE_PROJECT_ID.TABLE_DATASET_NAME.TABLE_NAME
FOR SYSTEM_TIME AS OF
  TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR);

bq cp \
--no_clobber \
--snapshot \
TABLE_PROJECT_ID:TABLE_DATASET_NAME.TABLE_NAME@-3600000 \
SNAPSHOT_PROJECT_ID:SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME
###############

#######restore snapshot table to a new table
CREATE TABLE TABLE_PROJECT_ID.TABLE_DATASET_NAME.NEW_TABLE_NAME
CLONE SNAPSHOT_PROJECT_ID.SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME;
---------------------------------

CREATE OR REPLACE TABLE TABLE_PROJECT_ID.TABLE_DATASET_NAME.TABLE_NAME
CLONE SNAPSHOT_PROJECT_ID.SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME;

CREATE SNAPSHOT TABLE SNAPSHOT_PROJECT_ID.SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME
CLONE TABLE_PROJECT_ID.TABLE_DATASET_NAME.TABLE_NAME
FOR SYSTEM_TIME AS OF
  TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR);

SELECT
  *
FROM
  PROJECT_ID.DATASET_NAME.INFORMATION_SCHEMA.TABLE_SNAPSHOTS;
---------------------------------
bq cp \
--restore \
--no_clobber \
SNAPSHOT_PROJECT_ID:SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME \
TABLE_PROJECT_ID:TABLE_DATASET_NAME.NEW_TABLE_NAME
------------------------------
bq cp \
--restore \
--force \
SNAPSHOT_PROJECT_ID:SNAPSHOT_DATASET_NAME.SNAPSHOT_NAME \
TABLE_PROJECT_ID:TABLE_DATASET_NAME.TABLE_NAME
---------------------------------

view metadata:

bq show \
--format=prettyjson \
PROJECT_ID:DATASET_NAME.SNAPSHOT_NAME

update metadata:

bq add-iam-policy-binding \
    --member="user:PRINCIPAL" \
    --role="roles/bigquery.dataViewer" \
    PROJECT_ID:DATASET_NAME.SNAPSHOT_NAME
##############################################

DROP SNAPSHOT TABLE PROJECT_ID.DATASET_NAME.SNAPSHOT_NAME;

bq rm \
PROJECT_ID:DATASET_NAME.SNAPSHOT_NAME