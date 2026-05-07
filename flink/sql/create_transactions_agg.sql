CREATE TABLE transactions_agg (
    window_start TIMESTAMP(3),
    window_end TIMESTAMP(3),
    account_id STRING,
    total_amount DOUBLE,
    txn_count BIGINT
) WITH (
    'connector' = 'print'
);