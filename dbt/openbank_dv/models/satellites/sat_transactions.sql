SELECT
    transaction_id,
    account_id AS hub_account_key,
    amount,
    transaction_type,
    transaction_timestamp,
    CURRENT_TIMESTAMP AS load_datetime,
    'openbank_system' AS record_source
FROM {{ ref('stg_transactions') }}