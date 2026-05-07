# OpenBank Lakehouse

Real-time + Batch Data Platform for Financial Transactions

---

# Architecture Overview

```text
1. Data Sources
   ├── Core Banking Systems
   ├── Mobile / Web Applications
   └── External Systems & Partners

                ↓

2. Ingestion Layer
   └── Apache Kafka
       └── Topic: transactions

                ↓

3. Stream Processing Layer
   └── Apache Flink
       ├── Event-time Processing
       ├── Watermarks
       ├── Stateful Processing
       └── Window Aggregations

                ↓

4. Lakehouse Storage (Snowflake)
   ├── BRONZE  → Raw Data
   ├── SILVER  → Cleaned Data
   └── GOLD    → Aggregated Metrics

                ↓

5. Consumption Layer
   ├── Dashboards / BI Tools
   ├── SQL Queries
   ├── APIs
   └── Data Science / ML

                ↑

6. Batch Processing
   └── Apache Spark
       ├── Reprocessing
       ├── Large Scale Aggregations
       ├── Data Quality Checks
       └── Feature Engineering

                ↑

7. Workflow Orchestration
   └── Apache Airflow
       ├── DAG Scheduling
       ├── Dependency Management
       ├── Monitoring & Alerts
       └── Retry Handling
```

---

# Tech Stack

| Layer             | Technology     |
| ----------------- | -------------- |
| Streaming         | Apache Kafka   |
| Stream Processing | Apache Flink   |
| Batch Processing  | Apache Spark   |
| Storage           | Snowflake      |
| Transformations   | dbt            |
| Orchestration     | Apache Airflow |
| Programming       | Python         |
| Containerization  | Docker         |

---

# Key Principles

* Event-time Processing
* Exactly-once Semantics
* Medallion Architecture
* Separation of Streaming and Batch Workloads
* Data Quality at Every Layer
* Scalable and Reliable Design

---

# Current Implementation Status

## Completed

* Kafka setup using Docker
* Real-time transaction producer in Python
* Kafka topic creation
* Flink SQL integration
* Event-time processing
* Watermark implementation
* Tumbling window aggregation
* Kafka upsert sink configuration
* Real-time aggregation pipeline

---

# Current Streaming Flow

```text
Python Producer
        ↓
Kafka Topic (transactions)
        ↓
Apache Flink SQL
        ↓
Window Aggregation
        ↓
Kafka Topic (transactions_agg)
```

---

# Planned Implementation

## Snowflake Layer

* Bronze Layer
* Silver Layer
* Gold Layer

## Batch Processing

* Spark-based reprocessing
* Large-scale aggregations
* Data quality validation

## Transformation Layer

* dbt models
* Curated business metrics

## Orchestration

* Airflow DAG scheduling
* Pipeline monitoring

---

# Project Structure

```text
openbank-lakehouse/
│
├── kafka/
│   ├── docker-compose.yml
│   └── producer.py
│
├── flink/
│   ├── docker-compose.yml
│   └── lib/
│
└── README.md
```

---

# How to Run

## Start Kafka

```bash
docker-compose -f kafka/docker-compose.yml up -d
```

## Start Flink

```bash
docker-compose -f flink/docker-compose.yml up -d
```

## Run Producer

```bash
python kafka/producer.py
```

## Open Flink SQL Client

```bash
docker exec -it jobmanager ./bin/sql-client.sh
```

---

# Engineering Challenges Solved

* Kafka Docker networking issues
* Kafka topic configuration
* Flink Kafka connector integration
* Event-time timestamp conversion
* Watermark configuration
* Append vs Update stream handling
* Upsert Kafka sink setup
* Flink resource allocation issues

---

# Future Scope

* Snowflake integration
* dbt transformations
* Airflow orchestration
* Production-grade deployment
* Monitoring and alerting

---

# LinkedIn Update

```text
Building a real-time streaming data pipeline as part of my OpenBank Lakehouse project.

Implemented:
• Kafka-based event streaming
• Apache Flink SQL for real-time processing
• Event-time processing with watermarking
• Tumbling window aggregations
• Kafka upsert sink for streaming aggregates
• Docker-based local orchestration

Key learnings:
• Streaming architecture design
• Event-time vs processing-time concepts
• Append vs update stream handling
• Kafka topic configuration
• Flink resource management
• Real-time aggregation challenges

Current architecture:
Python Producer → Kafka → Flink SQL → Aggregation → Kafka Sink

Next steps:
• Snowflake integration
• dbt transformations
• CDC ingestion
• Production-style lakehouse architecture

GitHub:
https://github.com/sidpanda-alt/openbank-lakehouse
```

---

# Git Commands

```bash
git add .
git commit -m "Implemented Kafka-Flink real-time streaming pipeline with event-time aggregation"
git push
```

---

# Author

Sidharth Panda

GitHub:
[https://github.com/sidpanda-alt/openbank-lakehouse](https://github.com/sidpanda-alt/openbank-lakehouse)
