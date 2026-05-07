INSERT INTO transactions_agg
SELECT
    window_start,
    window_end,
    account_id,
    CAST(SUM(amount) AS DECIMAL(10,2)) AS total_amount,
    COUNT(*) AS txn_count
FROM TABLE(
    TUMBLE(
        TABLE transactions,
        DESCRIPTOR(event_time),
        INTERVAL '10' SECONDS
    )
)
GROUP BY
    window_start,
    window_end,
    account_id;