# 🪙 Gold ETL Pipeline with Apache Airflow & Docker

This project is an **automated ETL pipeline** built using **Apache Airflow**, running inside **Docker Compose**.  
It automatically **extracts**, **transforms**, and **loads** daily gold price data from [GoldAPI.io](https://www.goldapi.io/) — perfect for practicing Data Engineering and pipeline orchestration.

---

## ⚙️ Features

- 🕒 **Automated scheduling** with Apache Airflow  
- 🌐 **Extract** gold price data from GoldAPI  
- 🧮 **Transform** raw JSON into structured DataFrame using pandas  
- 💾 **Load** data into PostgreSQL or export as CSV/email  
- 🐳 Fully **containerized** with Docker Compose  
- 📧 Optional email notifications with attached report  

---

## 📂 Project Structure

.
├── config/
│ └── airflow.cfg
│
├── dags/
│ └── gold_data_dag.py # Airflow DAG 
│
├── src/
│ ├── config.py # Load env variables
│ ├── extract.py # Fetch data from API
│ ├── transform.py # Clean & format data
│ ├── load.py # Send to email
│ └── main.py # Just for testing the ETL
│
├── docker-compose.yaml # Docker setup for Airflow
├── .env # Just the example environment variables =))
└── README.md

---

## 🧾 Example `.env` file

Copy `.env.example` → `.env` and fill your credentials:

```env
GOLD_API_URL=https://www.goldapi.io/api/XAU/USD
GOLD_API_KEY=get_your_api_key_on_website_https://www.goldapi.io/dashboard

AIRFLOW_UID=50000

GMAIL_USER=example@gmail.com
GMAIL_PASSWORD=your_app_password_here


