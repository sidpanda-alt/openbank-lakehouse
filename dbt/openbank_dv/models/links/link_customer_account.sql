SELECT DISTINCT
    customer_id AS hub_customer_key,
    account_id AS hub_account_key,
    CURRENT_TIMESTAMP AS load_datetime,
    'openbank_system' AS record_source
FROM {{ ref('stg_accounts') }}