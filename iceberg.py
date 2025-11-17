from pyspark.sql import SparkSession

# Initialize Spark Session

spark = SparkSession.builder \
        .appName("IcebergLocalSetup") \
        .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
        .config("spark.sql.catalog.local.type", "hadoop") \
        .config("spark.sql.catalog.local.warehouse", "file:///C:/iceberg_data_warehouse/w1/") \
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .config("spark.jars", "file:///C:/iceberg/iceberg-spark-runtime-4.0_2.13-1.10.0.jar") \
        .getOrCreate()