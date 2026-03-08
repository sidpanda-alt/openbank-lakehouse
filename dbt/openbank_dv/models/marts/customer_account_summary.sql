SELECT
    c.customer_id,
    COUNT(DISTINCT a.account_id) AS total_accounts,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_transaction_amount
FROM {{ ref('hub_customer') }} c
LEFT JOIN {{ ref('link_customer_account') }} l
    ON c.hub_customer_key = l.hub_customer_key
LEFT JOIN {{ ref('hub_account') }} a
    ON l.hub_account_key = a.hub_account_key
LEFT JOIN {{ ref('sat_transactions') }} t
    ON a.hub_account_key = t.hub_account_key
GROUP BY c.customer_id