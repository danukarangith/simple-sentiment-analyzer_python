from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    text = request.form['text']
    return analyze_sentiment(text)

if __name__ == '__main__':
    app.run(debug=True)
