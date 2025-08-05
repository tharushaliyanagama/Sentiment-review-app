from transformers import pipeline
import pandas as pd

# Load pre-trained models
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def analyze_sentiment(reviews):
    """Analyze sentiment of a list of reviews."""
    results = []
    for review in reviews:
        result = sentiment_analyzer(review)[0]
        label = result['label']
        score = result['score']
        sentiment = 'Positive' if label == 'POSITIVE' else 'Negative' if label == 'NEGATIVE' else 'Neutral'
        results.append({'review': review, 'sentiment': sentiment, 'confidence': score})
    return results

def summarize_reviews(reviews, summary_type):
    """Summarize a list of reviews based on the selected summary type."""
    combined_text = " ".join(reviews)
    if len(combined_text) < 50:
        return "Insufficient text for summarization."
    
    # Adjust summary parameters based on type
    if summary_type == "concise":
        summary = summarizer(combined_text, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
        return f"<p><strong>Concise Summary:</strong> {summary}</p>"
    elif summary_type == "detailed":
        summary = summarizer(combined_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        return f"<p><strong>Detailed Summary:</strong> {summary}</p>"
    elif summary_type == "bullet_points":
        summary = summarizer(combined_text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        points = summary.split('. ')
        return "<p><strong>Key Points:</strong></p><ul>" + "".join(f"<li>{point}</li>" for point in points if point) + "</ul>"
    elif summary_type == "key_insights":
        summary = summarizer(combined_text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        return f"<p><strong>Key Insights:</strong></p><p>{summary}</p>"
    else:
        return "Invalid summary type."