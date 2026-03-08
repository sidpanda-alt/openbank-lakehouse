SELECT DISTINCT
    customer_id AS hub_customer_key,
    customer_id,
    CURRENT_TIMESTAMP AS load_datetime,
    'openbank_system' AS record_source
FROM {{ ref('stg_customers') }}