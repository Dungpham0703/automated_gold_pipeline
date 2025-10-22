# 🪙 Automated Gold Data Pipeline (Airflow + Docker)

An automated **ETL pipeline** built using **Apache Airflow** and **Docker Compose**, designed to fetch, transform, and deliver **daily gold price data** directly to your email inbox 📧.

This project is ideal for practicing **Data Engineering**, **ETL orchestration**, and **workflow automation** using real-world tools.

---

## ✨ Key Features

* 🕒 **Automated Scheduling** — The pipeline runs daily through Apache Airflow.
* 🌐 **API Integration** — Fetches live gold price data from [GoldAPI.io](https://www.goldapi.io/).
* 🧮 **Data Transformation** — Cleans and formats JSON data into a structured CSV using `pandas`.
* 📧 **Email Automation** — Sends the processed CSV to your Gmail inbox via SMTP.
* 🐳 **Containerized Setup** — Runs entirely in Docker Compose for easy deployment and portability.

---

## 🗂 Project Structure

The project is organized for clarity and modularity:

```bash
automated_gold_pipeline/
├── config/               # Airflow configuration
├── dags/                 # DAG definition for ETL
├── src/                  # ETL scripts (extract, transform, load)
├── docker-compose.yaml   # Docker setup for Airflow services
├── .env.example          # Example environment variables
└── README.md             # Documentation

