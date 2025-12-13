# kafka_consumer.py  (EDIT THESE LINES)

from kafka import KafkaConsumer
import json
from spark.spark_processing import process_article


consumer = KafkaConsumer(
    "news_topic",
    bootstrap_servers=["localhost:29092"],  # <-- Confluent host port
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",           # <-- read from beginning if no committed offsets
    enable_auto_commit=True,                # okay for this demo
    group_id="news-consumer-1"              # fixed group id for visibility
)

print("[consumer] started, waiting for messages...")
for msg in consumer:
    try:
        article = msg.value
        print("[consumer] got message:", article.get("title", "")[:80])
        process_article(article)
    except Exception as e:
        # Don't fail silently—show what went wrong
        print("[consumer] ERROR processing message:", repr(e))
