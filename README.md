# 🪙 Gold ETL Pipeline (Airflow + Docker)

An automated **ETL pipeline** built with **Apache Airflow** and **Docker Compose**.  
It extracts daily **gold price data** from [GoldAPI.io](https://www.goldapi.io/), transforms it with **pandas**, and **sends the result via email** as a CSV attachment.

---

## ⚙️ Features

- 🕒 Automated scheduling with Apache Airflow  
- 🌐 Extract gold price data from GoldAPI  
- 🧮 Transform JSON into a clean pandas DataFrame  
- 📧 Send cleaned data as CSV via Gmail SMTP  
- 🐳 Fully containerized setup using Docker Compose  

---

## 📂 Project Structure

.
├── config/
│ └── airflow.cfg # Airflow configuration file
│
├── dags/
│ └── gold_data_dag.py # Main Airflow DAG (Extract → Transform → Send Email)
│
├── src/
│ ├── config.py # Load environment variables
│ ├── extract.py # Fetch data from GoldAPI
│ ├── transform.py # Clean and format the raw data
│ ├── load.py # Send processed data to email
│ └── main.py # Run ETL manually for testing
│
├── docker-compose.yaml # Docker setup for Airflow
├── .env.example # Example environment variables
└── README.md # Project documentation

yaml
Copy code

---

## ⚡ Quick Start

### 🧩 1. Clone the repository
```bash
git clone https://github.com/Dungpham0703/gold_etl_pipeline.git
cd gold_etl_pipeline
⚙️ 2. Create your .env file
Duplicate the example:

bash
Copy code
cp .env.example .env
Then edit .env:

env
Copy code
GOLD_API_URL=https://www.goldapi.io/api/XAU/USD
GOLD_API_KEY=your_api_key_here

AIRFLOW_UID=50000

GMAIL_USER=youremail@gmail.com
GMAIL_PASSWORD=your_app_password
⚠️ Use a Google App Password (not your regular Gmail password).
You can create one here: https://myaccount.google.com/apppasswords

🐳 3. Run Docker & Airflow
bash
Copy code
docker compose up --build
Wait until containers are ready, then open:
👉 http://localhost:8080

Default Airflow login:

makefile
Copy code
Username: airflow
Password: airflow
🚀 Running the DAG
1️⃣ Go to Airflow Web UI
2️⃣ Find the DAG named gold_data_dag
3️⃣ Click Trigger DAG ▶️ to start the ETL manually
4️⃣ Watch logs for each step:

extract_task → fetches gold data from API

transform_task → cleans and structures data

load_task → sends the CSV report to your Gmail

🧠 Run ETL manually (without Airflow)
You can test your ETL script locally:

bash
Copy code
python src/main.py
This will:

Call the GoldAPI endpoint

Transform the JSON data into a DataFrame

Save it as a CSV and send it to your Gmail

Example main.py:

python
Copy code
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

if __name__ == "__main__":
    df = extract_data()
    df = transform_data(df)
    load_data(df, date_str="2025-10-22")
🧰 Common Docker Commands
bash
Copy code
# Start Airflow services
docker compose up -d

# Stop and remove containers
docker compose down

# View running containers
docker ps

# View logs from Airflow scheduler
docker logs airflow-scheduler

# Enter the Airflow webserver container
docker exec -it airflow-webserver bash
🧩 DAG Overview
css
Copy code
Extract → Transform → Send Email
Step	Task ID	Description
1️⃣	extract_task	Fetch data from GoldAPI
2️⃣	transform_task	Clean & normalize the data
3️⃣	load_task	Send cleaned CSV to Gmail inbox

🧠 Tech Stack
Tool	Purpose
Python 3.12	Core ETL logic
Apache Airflow	Orchestration and scheduling
Docker Compose	Container management
Pandas	Data transformation
smtplib (Gmail SMTP)	Email sending

👤 Author
Phạm Thanh Dũng
🎓 Troy Campus @ Duy Tân University
🌐 GitHub: Dungpham0703
📧 phamthanhdung1112@gmail.com

📜 License
MIT License © 2025 Phạm Thanh Dũng

yaml
Copy code

---

This version:
- ✅ Removes PostgreSQL mentions  
- ✅ Emphasizes the **email-only load step**  
- ✅ Includes runnable Docker and Python code  
- ✅ Looks professional and clean for GitHub  

Would you like me to make a **shorter version** of this (a “Quick Setup” summary for the top of README, like a TL;DR with only commands)?
