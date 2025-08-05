from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
from model import analyze_sentiment, summarize_reviews

app = Flask(__name__)

def fetch_reviews(restaurant_name):
    try:
        with open('data/factual_tripadvisor_restaurant_data_all_100_reviews.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)       
        for restaurant in data['restaurants']:
            if restaurant_name.lower() in restaurant['name'].lower():
                return [review['review_text'] for review in restaurant['reviews'][:10] if 'review_text' in review and len(review['review_text'].strip()) > 0]
        return []
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    summary = ""
    error = ""
    restaurant_name = ""
    summary_type = "concise"  # Default summary type
    if request.method == 'POST':
        restaurant_name = request.form.get('restaurant_name', '')
        summary_type = request.form.get('summary_type', 'concise')
        if not restaurant_name:
            error = "Please enter a restaurant name."
        else:
            reviews = fetch_reviews(restaurant_name)
            if reviews:
                results = analyze_sentiment(reviews)
                summary = summarize_reviews(reviews, summary_type)
            else:
                error = f"No reviews found for '{restaurant_name}'."
    return render_template('index.html', results=results, summary=summary, error=error, restaurant_name=restaurant_name, summary_type=summary_type)

if __name__ == '__main__':
    app.run(debug=True)