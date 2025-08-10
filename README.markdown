# AI-Powered Sentiment Analysis and Review Summarization Web App

## Overview
A Flask-based web app for analyzing restaurant review sentiments using BERT and summarizing reviews using BART.Built backend development and API/CLI skills. Uses a JSON dataset of 5,700 reviews from 57 San Francisco Bay Area restaurants.

## Features
- Sentiment analysis of restaurant reviews using DistilBERT (Positive/Negative/Neutral).
- Summarization of reviews using BART with options for concise, detailed, bullet points, or key insights.
- Modern Flask web interface with tabbed results and loading animation.
- Processes JSON data from TripAdvisor and Factual API.
- CLI-driven setup and deployment.

## Dataset
A JSON file (`data/restaurant_reviews.json`) containing 5,700 reviews for 57 San Francisco Bay Area restaurants (100 reviews each) from TripAdvisor, with metadata from the Factual API.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment_review_app.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Usage
- Visit `http://localhost:5000`.
- Enter a restaurant name (e.g., "The Stinking Rose") and select a summary type.
- View sentiment analysis and summary in a tabbed interface.

## Screenshots
![Dashboard](screenshots/dashboard.png)

