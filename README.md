# real-time-product-analytics-platform
Production-grade real-time data engineering platform implementing Landing → Bronze → Silver → Gold architecture with streaming and batch pipelines, data quality, observability, dimensional modeling, and business analytics using Kafka, Spark, Airflow, and AWS.


## Overview
This project implements a production-grade real-time data platform for a
product-based company. It processes both streaming and batch data using a
full Medallion Architecture (Landing, Bronze, Silver, Gold) and delivers
analytics-ready datasets, data quality guarantees, observability, and
business dashboards.

## Problem Statement
Modern product companies need scalable and reliable data platforms to:
- Capture real-time user behavior
- Process high-volume event streams
- Maintain data quality and trust
- Enable fast, reliable business analytics

This project simulates a real-world internal data platform solving these challenges.

## Architecture Highlights
- Streaming and batch pipelines
- Landing → Bronze → Silver → Gold architecture
- Dimensional modeling (fact & dimension tables)
- Data quality checks and observability
- AI-assisted data workflows
- Business-ready dashboards

## Tech Stack
- **Languages**: Python, SQL
- **Streaming**: Apache Kafka, Spark Structured Streaming
- **Batch Processing**: PySpark
- **Orchestration**: Apache Airflow
- **Storage**: AWS S3 (Data Lake)
- **Metadata & Query**: AWS Glue, Athena
- **Warehouse**: Amazon Redshift / Snowflake
- **Visualization**: QuickSight / Superset / Metabase
- **Cloud**: AWS

## Data Layers
- **Landing**: Raw immutable ingested data
- **Bronze**: Parsed and validated raw data
- **Silver**: Cleaned and enriched data
- **Gold**: Business-ready fact and dimension tables

## Project Status
🚧 In Progress  
Day 1: Project charter, architecture, and scope definition
