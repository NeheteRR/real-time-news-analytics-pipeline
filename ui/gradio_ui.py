import gradio as gr
from database.mongodb_connect import get_articles

def display_news():
    articles = get_articles()

    if not articles:
        return "No news articles found."

    output = []
    for a in articles:
        title = a.get("title", "No Title")
        sentiment = a.get("sentiment", 0.0)
        output.append(f"📰 {title}\n   Sentiment Score: {sentiment:.2f}")

    return "\n\n".join(output)


with gr.Blocks(title="Real-Time News Analytics") as demo:
    gr.Markdown("## 📰 Real-Time News Analytics Dashboard")
    gr.Markdown("Latest news headlines with sentiment scores")

    output_box = gr.Textbox(
        label="News Output",
        lines=15,          # ⬅ Bigger output box
        max_lines=25,
        interactive=False
    )

    refresh_btn = gr.Button("🔄 Refresh News")

    # Load data on page load
    demo.load(display_news, outputs=output_box)

    # Refresh button
    refresh_btn.click(display_news, outputs=output_box)

demo.launch()
