# 📰 Real-Time News Analytics Pipeline

A **real-time news analytics system** built using **Apache Airflow, Apache Kafka, Apache Spark, and MongoDB**.

This pipeline fetches live news articles from the **News API**, streams them through **Kafka**, performs **sentiment analysis**, stores the processed data in **MongoDB**, and provides **CRUD operations** along with a **Gradio-based UI** to view results.

This project demonstrates an **end-to-end big data pipeline** using modern data engineering tools.

---

## 🚀 Features

- 🔄 Real-time data ingestion from News API  
- 📡 Streaming with Apache Kafka  
- ⚙️ Workflow orchestration using Apache Airflow  
- 🧠 Sentiment analysis using Apache Spark (PySpark) + TextBlob  
- 🗄️ MongoDB for persistent storage  
- ✏️ CRUD operations (Create, Read, Update, Delete)  
- 🖥️ Gradio UI for viewing news headlines and sentiment scores  
- 🐳 Docker-based setup for Kafka & MongoDB  

---

## 🛠️ Technology Stack

| Layer          | Technology              |
|---------------|--------------------------|
| Orchestration | Apache Airflow           |
| Streaming     | Apache Kafka             |
| Processing    | Apache Spark (PySpark)   |
| NLP           | TextBlob                 |
| Database      | MongoDB                  |
| UI            | Gradio                   |
| Language      | Python                   |
| Deployment    | Docker                   |

---

## 📁 Project Structure

```text
real-time-news-analytics-pipeline/
│
├── dags/                     # Airflow DAGs
│   └── airflow_dag.py
│
├── kafka/                    # Kafka producer & consumer
│   ├── kafka_producer.py
│   └── kafka_consumer.py
│
├── spark/                    # Spark processing logic
│   └── spark_processing.py
│
├── database/                 # MongoDB connection & CRUD
│   ├── mongodb_connect.py
│   └── crud_operations.py
│
├── ui/                       # Gradio UI
│   └── gradio_ui.py
│
├── docker/                   # Docker configuration
│   └── compose.yml
│
├── logs/                     # Application logs
├── docs/                     # Project documentation
│
├── requirements.txt
├── .gitignore
└── README.md 
```

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Prerequisites
Ensure the following are installed:
- Python **3.9 or 3.10**
- Docker Desktop (**WSL 2 enabled**)
- Java **JDK 8 or 11**
- Git

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/real-time-news-analytics-pipeline.git
cd real-time-news-analytics-pipeline
```

3️⃣ Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

4️⃣ Start Kafka & MongoDB (Docker)
```bash
cd docker
docker compose up -d
docker ps   #Verify
```

5️⃣ Start Airflow Scheduler

Airflow webserver runs in Docker, but the scheduler must be started to execute DAGs.
``bash
docker exec -it airflow bash
airflow scheduler
```
📌 Keep this scheduler running in the terminal.

6️⃣ Access Airflow UI
Open your browser:http://localhost:8080

Login credentials:
Username: admin
Password: admin
Enable the DAG: news_api_pipeline
Trigger the DAG manually ▶

7️⃣ Run Kafka Consumer
```bash
python kafka/kafka_consumer.py
#(Keep this terminal running)
```

8️⃣ Run Kafka Producer
```bash
python kafka/kafka_producer.py
This fetches live news and streams it to Kafka.
```

9️⃣ Verify MongoDB Storage
```bash
python database/crud_operations.py
```

🔟 Run Gradio UI
```bash
python -m ui.gradio_ui
```

⏰ Airflow DAG
- DAG Name: news_api_pipeline
- Schedule: Hourly
- Task: Fetch news → Publish to Kafka

🔄 Workflow Overview
- Airflow schedules the pipeline
- Kafka Producer fetches news from News API
- Kafka Consumer receives articles
- Spark processes text and computes sentiment
- MongoDB stores processed articles
- Gradio UI displays results

📊 Sample Output
- Title: News headline
- Sentiment Score: Range from -1 (negative) to +1 (positive)