CREATE TABLE transactions (
    txn_id STRING,
    account_id STRING,
    amount DOUBLE,
    ts DOUBLE,

    event_time AS TO_TIMESTAMP_LTZ(CAST(ts * 1000 AS BIGINT), 3),

    WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
) WITH (
    'connector' = 'kafka',
    'topic' = 'transactions',
    'properties.bootstrap.servers' = 'kafka:9092',
    'properties.group.id' = 'flink-group',
    'format' = 'json',
    'scan.startup.mode' = 'latest-offset'
);