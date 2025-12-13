# spark_processing.py  (ADD prints and try/except around insert)

from pyspark.sql import SparkSession
from textblob import TextBlob
from mongodb_connect import insert_article

spark = SparkSession.builder.appName("NewsProcessing").getOrCreate()

def process_article(article):
    try:
        title = article.get("title", "")
        description = article.get("description", "") or ""
        sentiment = TextBlob(description).sentiment.polarity

        processed = {
            "title": title,
            "description": description,
            "sentiment": float(sentiment),
        }
        insert_article(processed)
        print("[spark] inserted:", title[:80], f"(sentiment={sentiment:.2f})")
    except Exception as e:
        print("[spark] ERROR:", repr(e))
