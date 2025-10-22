# 🪙 Automated Gold Data Pipeline (Airflow + Docker)

An automated **ETL pipeline** built using **Apache Airflow** and **Docker Compose**, designed to fetch, transform, and deliver **daily gold price data** directly to your email inbox 📧.

---

## ✨ Key Features

* 🕒 **Automated Scheduling** — The pipeline runs daily through Apache Airflow.
* 🌐 **API Integration** — Fetches live gold price data from [GoldAPI.io](https://www.goldapi.io/).
* 🧮 **Data Transformation** — Cleans and formats JSON data into a structured CSV using pandas.
* 📧 **Email Automation** — Sends the processed CSV to your Gmail inbox via SMTP.
* 🐳 **Containerized Setup** — Runs entirely in Docker Compose for easy deployment and portability.

---

## 🗂 Project Structure

The project is organized for clarity and modularity:

```bash
automated_gold_pipeline/
├── config/               # Airflow configuration
├── dags/                 # gold DAG
├── src/                  # ETL scripts (extract, transform, load)
├── docker-compose.yaml   # Docker setup for Airflow services
├── .env                  # Just example, not real environment variables
└── README.md             # Documentation
```
---

## 🚀 Getting Started

Follow these steps to set up and run the ETL pipeline on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Dungpham0703/gold_etl_pipeline.git
cd gold_etl_pipeline
```
### 2️⃣ Create a Google App Password (for Gmail)

Since Gmail no longer allows direct SMTP login with your normal password,  
you must create a **Google App Password** to let Airflow send emails securely.

Follow these steps:

1. Go to **Google Account → Security → 2-Step Verification**  
   👉 [https://myaccount.google.com/security](https://myaccount.google.com/security)

2. Turn on **2-Step Verification**.

3. Then open **App Passwords**  
   👉 [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

4. Choose:
   - **App:** Other (Custom name) → type `Gold_ETL_Pipeline`
   - **Device:** Your computer

5. Click **Generate**, copy the 16-character password Google gives you.

6. Paste it into your `.env` file like this:
   ```env
   GMAIL_USER=youremail@gmail.com
   GMAIL_PASSWORD=abcd efgh ijkl mnop
   
### 3️⃣ Set Up Environment Variables
```bash
GOLD_API_URL=https://www.goldapi.io/api/XAU/USD
GOLD_API_KEY= get_your_api_key_at_https://www.goldapi.io/dashboard
AIRFLOW_UID=50000
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password
```
### 4️⃣ Start Airflow with Docker
Running the Docker then:
```bash
docker compose up -d
```
After setup completes, open Airflow in your browser at localhost:8080
Default credentials:
```bash
Username: airflow
Password: airflow
```
### 5️⃣ Run the DAG

Open Airflow, find the DAG named gold_data_dag, and trigger it manually and you will know how high gold price is through email.

Each task performs the following:

Extract data from API -> Transform with pandas -> Send CSV file to your email.

### 6️⃣ Stop All Containers

Stop the Airflow environment cleanly:
```bash
docker compose down
```


load_task → Sends the cleaned CSV to your Gmail inbox
