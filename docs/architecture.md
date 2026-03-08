# OpenBank Lakehouse Architecture

This project demonstrates a modern lakehouse architecture for a banking analytics platform.

## Architecture Overview

             +----------------------+
             |   Sample Data (CSV)  |
             +----------------------+
                        |
                        v
               Spark Ingestion
                        |
                        v
                Bronze Layer
              (Raw Parquet Files)
                        |
                        v
            Spark Transformation
                        |
                        v
                Silver Layer
             (Clean Parquet Files)
                        |
                        v
                dbt Staging Models
                        |
                        v
                  DuckDB Warehouse
                        |
                        v
                Gold Analytics Layer
                        |
                        v
                BI / Data Science


## Data Flow

1. Raw banking data is ingested using Apache Spark
2. Data is stored in Bronze layer as raw parquet files
3. Spark cleans and transforms data into Silver layer
4. dbt creates staging models
5. Data is loaded into DuckDB warehouse
6. Analytics-ready models are created in Gold layer