SELECT
    customer_id,
    first_name,
    last_name,
    email,
    city,
    created_at,
    ingestion_timestamp
FROM read_parquet('D:/projects/openbank-lakehouse/data/silver/customers/*.parquet')