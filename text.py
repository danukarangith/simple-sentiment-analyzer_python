import nltk
from textblob import TextBlob
from tkinter import Tk, Label, Entry, Button, StringVar

# Download necessary corpora
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

 
def analyze_sentiment():
    text = user_input.get()
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        sentiment_result.set("Positive")
    elif sentiment < 0:
        sentiment_result.set("Negative")
    else:
        sentiment_result.set("Neutral")

 
root = Tk()
root.title("Sentiment Analysis")

 
Label(root, text="Enter text:").pack(pady=10)
user_input = Entry(root, width=50)
user_input.pack(pady=10)

Button(root, text="Analyze Sentiment", command=analyze_sentiment, bg='yellow', fg='black').pack(pady=10)

 
sentiment_result = StringVar()
sentiment_label = Label(root, textvariable=sentiment_result, font=("Helvetica", 16))
sentiment_label.pack(pady=20)
 
root.mainloop()
