CREATE TABLE transactions_agg (
    window_start TIMESTAMP(3),
    window_end TIMESTAMP(3),
    account_id STRING,
    total_amount DECIMAL(10,2),
    txn_count BIGINT,

    PRIMARY KEY (window_start, window_end, account_id) NOT ENFORCED
) WITH (
    'connector' = 'upsert-kafka',
    'topic' = 'transactions_agg',
    'properties.bootstrap.servers' = 'kafka:9092',

    'key.format' = 'json',
    'value.format' = 'json'
);