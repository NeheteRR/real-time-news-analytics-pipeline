import gradio as gr
from database.mongodb_connect import get_articles

def display_news():
    articles = get_articles()
    return [f"{a['title']} ({a['sentiment']:.2f})" for a in articles]

iface = gr.Interface(fn=display_news, inputs=[], outputs="text")
iface.launch()