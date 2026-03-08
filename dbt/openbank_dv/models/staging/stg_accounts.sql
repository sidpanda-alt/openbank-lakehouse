SELECT
    account_id,
    customer_id,
    account_type,
    balance,
    created_at,
    ingestion_timestamp
FROM read_parquet('D:/projects/openbank-lakehouse/data/silver/accounts/*.parquet')