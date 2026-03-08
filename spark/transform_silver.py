from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("OpenBank Silver Transformation") \
    .getOrCreate()

BRONZE_PATH = "/data/bronze"
SILVER_PATH = "/data/silver"

# -------------------------
# Customers
# -------------------------
customers = spark.read.parquet(f"{BRONZE_PATH}/customers")

customers_clean = customers \
    .dropDuplicates(["customer_id"]) \
    .withColumn("created_at", col("created_at").cast("timestamp"))

customers_clean.write.mode("overwrite").parquet(f"{SILVER_PATH}/customers")

# -------------------------
# Accounts
# -------------------------
accounts = spark.read.parquet(f"{BRONZE_PATH}/accounts")

accounts_clean = accounts \
    .dropDuplicates(["account_id"]) \
    .withColumn("balance", col("balance").cast("double")) \
    .withColumn("created_at", col("created_at").cast("timestamp"))

accounts_clean.write.mode("overwrite").parquet(f"{SILVER_PATH}/accounts")

# -------------------------
# Transactions
# -------------------------
transactions = spark.read.parquet(f"{BRONZE_PATH}/transactions")

transactions_clean = transactions \
    .dropDuplicates(["transaction_id"]) \
    .withColumn("amount", col("amount").cast("double")) \
    .withColumn("transaction_timestamp", col("transaction_timestamp").cast("timestamp"))

transactions_clean.write.mode("overwrite").parquet(f"{SILVER_PATH}/transactions")

print("Silver transformation complete")

spark.stop()