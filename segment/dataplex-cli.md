########

LAKE   ---->  ZONE --->   ASSET
########
In Dataplex, a lake is the highest organizational domain that represents a specific data
area or business unit

gcloud dataplex lakes create ecommerce \
   --location=$REGION \
   --display-name="Ecommerce" \
   --description="Ecommerce Domain"
#############################################
After you create a lake, you can add zones to the lake. Zones are subdomains within a lake that you can use to categorize data further. For example, you can categorize data by stage, usage, or restrictions.

There are two types of zones:

Raw zones contain data in raw formats (such as files in Cloud Storage buckets) and are not subject to strict type-checking.
Curated zones contain data that is cleaned, formatted, and ready for analytics such as BigQuery datasets.
#########
gcloud dataplex zones create orders-curated-zone \
    --location=$REGION \
    --lake=ecommerce \
    --display-name="Orders Curated Zone" \
    --resource-location-type=SINGLE_REGION \
    --type=CURATED \
    --discovery-enabled \
    --discovery-schedule="0 * * * *"

########

bq mk --location=$REGION --dataset orders 
###
Delete
----------------------------
gcloud dataplex assets delete orders-curated-dataset --location=$REGION --zone=orders-curated-zone --lake=ecommerce 

gcloud dataplex zones delete orders-curated-zone --location=$REGION --lake=ecommerce

gcloud dataplex lakes delete ecommerce --location=$REGION
---------------------
 OpenLineage is an open platform for collecting and analyzing data lineage information that is used by data professionals to capture lineage events from data pipeline components which use an OpenLineage API such as Apache Airflow, Apache Spark, and dbt. With the Data Lineage API, you can manually add lineage information for any non-natively supported data sources, including data transformations jobs that occurred outside of the Google Cloud project.

 ==============
 gcurl -X POST https://datalineage.googleapis.com/v1/projects/qwiklabs-gcp-02-2449fb7735ff/locations/us-west1:searchLinks -d "$(cat <<EOF
{ 
"source": { "fullyQualifiedName": "bigquery:qwiklabs-gcp-02-2449fb7735ff.qwiklabs_bank.ATM_Transaction_Raw"
}
}
EOF
)"

DATAPLEX_ENTRY_NAME="projects/132901694957/locations/us-west1/entryGroups/@bigquery/entries/bigquery.googleapis.com/projects/qwiklabs-gcp-02-2449fb7735ff/datasets/qwiklabs_bank/tables/ATM_Transaction_Fact"