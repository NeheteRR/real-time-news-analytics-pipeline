import requests
from kafka import KafkaProducer
import json, requests

API_KEY = "50338a87101442edbe299bc455378274"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

producer = KafkaProducer(
    bootstrap_servers=["kafka:29092"],   # Confluent host listener
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    acks="all",                              # wait for leader + ISR
    retries=5,                               # simple retry
    linger_ms=20,                            # small batching helps
    request_timeout_ms=30000,
    max_block_ms=120000
)

def fetch_and_publish_news():
    response = requests.get(URL)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        for article in articles:
            #producer.send("news_topic", article)
            fut = producer.send("news_topic", article)
            # block until the broker acks this record (or timeout)
            fut.get(timeout=30)
        producer.flush(30)   # wait up to 30s for any in-flight records
        producer.close(10)   # close nicely; give 10s to finish
        print(f"Published {len(articles)} articles to Kafka")
        print(f"Published {len(articles)} articles to Kafka")
    else:
        print("Failed to fetch news")

if __name__ == "__main__":
    fetch_and_publish_news()
