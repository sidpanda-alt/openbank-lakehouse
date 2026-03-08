# OpenBank Lakehouse

End-to-end **Lakehouse Data Engineering project** demonstrating a modern
analytics architecture using **Apache Spark, dbt, DuckDB, and Docker**.

This project simulates a banking data platform implementing a **Bronze →
Silver → Data Vault → Gold** pipeline.

------------------------------------------------------------------------

# Architecture

Bronze → Silver → Data Vault → Gold

![Architecture](docs/images/architecture.png)

Detailed architecture documentation:

docs/architecture.md

------------------------------------------------------------------------

# Tech Stack

  Layer              Tool
  ------------------ --------------
  Processing         Apache Spark
  Storage            Parquet
  Modeling           dbt
  Warehouse          DuckDB
  Containerization   Docker

------------------------------------------------------------------------

# Project Structure

    openbank-lakehouse
    │
    ├── airflow/                 # Airflow DAGs (future orchestration)
    │
    ├── data/
    │   ├── bronze/              # Raw ingested data
    │   ├── silver/              # Cleaned data
    │   └── gold/                # Analytics-ready data
    │
    ├── dbt/
    │   └── openbank_dv/
    │       ├── models/
    │       │   ├── staging
    │       │   ├── hubs
    │       │   ├── links
    │       │   ├── satellites
    │       │   └── marts
    │       └── dbt_project.yml
    │
    ├── docs/
    │   ├── architecture.md
    │   └── images/
    │       └── architecture.png
    │
    ├── sample_data/             # Raw sample banking datasets
    │
    ├── spark/
    │   ├── Dockerfile
    │   ├── ingest_bronze.py
    │   └── transform_silver.py
    │
    ├── warehouse/
    │   └── openbank.duckdb      # DuckDB analytics warehouse
    │
    ├── docker-compose.yml
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

# Pipeline Flow

### 1. Data Ingestion (Bronze Layer)

Raw banking datasets are ingested using **Spark** and stored as
**Parquet files**.

Example datasets:

-   Customers
-   Accounts
-   Transactions

Spark script:

    spark/ingest_bronze.py

Output:

    data/bronze/*

------------------------------------------------------------------------

### 2. Data Transformation (Silver Layer)

Spark cleans and standardizes the raw data.

Tasks include:

-   Data type standardization
-   Column normalization
-   Data quality checks

Spark script:

    spark/transform_silver.py

Output:

    data/silver/*

------------------------------------------------------------------------

### 3. Data Modeling (dbt)

dbt builds staging and transformation models on top of the **Silver
layer**.

Example staging models:

    stg_customers
    stg_accounts
    stg_transactions

Location:

    dbt/openbank_dv/models/staging

------------------------------------------------------------------------

### 4. Analytics Warehouse (DuckDB)

dbt loads analytics-ready tables into a **DuckDB warehouse**.

Warehouse file:

    warehouse/openbank.duckdb

------------------------------------------------------------------------

# Running The Project

## 1. Start the environment

    docker compose up -d

------------------------------------------------------------------------

## Run Full Pipeline

    python run_pipeline.py

------------------------------------------------------------------------

## 2. Enter the Spark container

    docker exec -it openbank_spark bash

------------------------------------------------------------------------

## 3. Run Bronze ingestion

    python3 ingest_bronze.py

------------------------------------------------------------------------

## 4. Run Silver transformation

    python3 transform_silver.py

------------------------------------------------------------------------

## 5. Run dbt models

Navigate to the dbt project:

    cd dbt/openbank_dv

Run models:

    dbt run

------------------------------------------------------------------------

# Example Output

After pipeline execution:

Bronze layer

    data/bronze/customers
    data/bronze/accounts
    data/bronze/transactions

Silver layer

    data/silver/customers
    data/silver/accounts
    data/silver/transactions

DuckDB tables

    stg_customers
    stg_accounts
    stg_transactions

------------------------------------------------------------------------

# Future Improvements

-   Add **Airflow orchestration**
-   Implement **Data Vault models**
-   Add **data quality tests**
-   Add **Gold analytics marts**

------------------------------------------------------------------------

# Author

**Siddharth Panda**

Senior Data Engineering Portfolio Project
