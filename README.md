
Airflow Bikeshare ETL Pipeline

This project is an Apache Airflow–orchestrated ETL pipeline that ingests bikeshare data and determines the location with the most bikes currently available. It demonstrates production-style data engineering patterns using Python and Airflow.

Project Overview

The pipeline extracts live bikeshare network data from a public API, processes station-level availability, and identifies the station (or location) with the highest number of available bikes at runtime.

The workflow is fully automated and scheduled using Apache Airflow, making it easy to monitor, retry, and extend.

Tech Stack

Python – Data extraction, transformation, and business logic

Apache Airflow – Workflow orchestration and scheduling

REST API – Source of bikeshare network and station data

Docker / EC2 (optional) – Deployment and execution environment

AWS S3 (optional) – Storage for processed outputs

Pipeline Flow

Extract

Fetch bikeshare network data from the public CityBikes API

Retrieve detailed station data for selected networks

Transform

Parse station-level availability

Aggregate available bike counts

Identify the station/location with the most bikes available

Load

Persist results (e.g., JSON or CSV)

Optionally upload output to an S3 bucket

DAG Structure
airflow_bikeshare_pipeline/
├── dags/
│   └── bikeshare_dag.py
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── requirements.txt
└── README.md

Scheduling

The DAG runs on a configurable schedule (every 15 mins)

Supports retries and failure handling via Airflow operators

Can be triggered manually from the Airflow UI

Getting Started
Prerequisites

Python 3.9+

Apache Airflow

API access to CityBikes (no auth required)

Setup
git clone https://github.com/your-username/airflow_bikeshare_pipeline.git
cd airflow_bikeshare_pipeline
pip install -r requirements.txt


Initialize Airflow:

airflow db init
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com


Start Airflow:

airflow webserver
airflow scheduler


Access the UI at:
http://localhost:8080

Example Output
{
  "station_name": "Market St & 7th St",
  "city": "San Francisco",
  "available_bikes": 42,
  "timestamp": "2026-01-07T12:00:00Z"
}

Future Improvements

Add historical storage and trend analysis

Support multiple cities and networks

Load results into a data warehouse (Redshift / BigQuery)

Add data quality checks and alerting

Visualize results with a dashboard

Why This Project?

This pipeline demonstrates:

Real-world API ingestion

Modular ETL design

Airflow DAG orchestration

Cloud-ready data engineering practices

Built as part of a growing portfolio focused on Data Engineering and Cloud Engineering.
