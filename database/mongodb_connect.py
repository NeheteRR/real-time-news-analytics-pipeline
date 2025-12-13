import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["news_db"]
collection = db["articles"]

def insert_article(article):
    collection.insert_one(article)

def get_articles():
    return list(collection.find())

def update_article(query, new_values):
    collection.update_one(query, {"$set": new_values})

def delete_article(query):
    collection.delete_one(query)
