SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_transaction_amount
FROM {{ ref('sat_transactions') }}
GROUP BY transaction_type