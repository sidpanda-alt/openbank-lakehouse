from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

# Create Spark session
spark = SparkSession.builder \
    .appName("OpenBank Bronze Ingestion") \
    .getOrCreate()

# Paths
INPUT_PATH = "/sample_data"
BRONZE_PATH = "/data/bronze"

# -----------------------------
# Customers
# -----------------------------
customers = spark.read.option("header", True).csv(f"{INPUT_PATH}/customers.csv")

customers = customers.withColumn("ingestion_timestamp", current_timestamp())

customers.write.mode("overwrite").parquet(f"{BRONZE_PATH}/customers")

# -----------------------------
# Accounts
# -----------------------------
accounts = spark.read.option("header", True).csv(f"{INPUT_PATH}/accounts.csv")

accounts = accounts.withColumn("ingestion_timestamp", current_timestamp())

accounts.write.mode("overwrite").parquet(f"{BRONZE_PATH}/accounts")

# -----------------------------
# Transactions
# -----------------------------
transactions = spark.read.option("header", True).csv(f"{INPUT_PATH}/transactions.csv")

transactions = transactions.withColumn("ingestion_timestamp", current_timestamp())

transactions.write.mode("overwrite").parquet(f"{BRONZE_PATH}/transactions")

print("Bronze ingestion complete")

spark.stop()