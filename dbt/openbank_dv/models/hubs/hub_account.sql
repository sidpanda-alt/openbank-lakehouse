SELECT DISTINCT
    account_id AS hub_account_key,
    account_id,
    CURRENT_TIMESTAMP AS load_datetime,
    'openbank_system' AS record_source
FROM {{ ref('stg_accounts') }}