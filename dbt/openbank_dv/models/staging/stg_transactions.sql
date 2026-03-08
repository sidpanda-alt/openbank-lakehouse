SELECT
    transaction_id,
    account_id,
    amount,
    transaction_type,
    transaction_timestamp,
    ingestion_timestamp
FROM read_parquet('D:/projects/openbank-lakehouse/data/silver/transactions/*.parquet')