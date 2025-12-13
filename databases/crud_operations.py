from mongodb_connect import insert_article, get_articles, update_article, delete_article
from database.mongodb_connect import insert_article, get_articles, update_article, delete_article

# Example CRUD operations
if __name__ == "__main__":
    # Create
    insert_article({"title": "Sample News", "description": "Test news", "sentiment": 0.1})

    # Read
    print(get_articles())

    # Update
    update_article({"title": "Sample News"}, {"description": "Updated description"})

    # Delete
    delete_article({"title": "Sample News"})
