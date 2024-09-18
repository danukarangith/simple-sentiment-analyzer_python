from tkinter import Tk, Label, Entry, Button, StringVar, filedialog
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to handle file upload
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            sentiment_result.set(analyze_sentiment(text))

# Create the main window
root = Tk()
root.title("Sentiment Analysis")

# Create a label, entry, and button for user input
Label(root, text="Enter text:").pack(pady=10)
user_input = Entry(root, width=50)
user_input.pack(pady=10)

# Create a button for analyzing text from the entry widget
Button(root, text="Analyze Text", command=lambda: sentiment_result.set(analyze_sentiment(user_input.get())), bg='blue', fg='white').pack(pady=10)

# Create a button for uploading and analyzing a text file
Button(root, text="Upload File", command=upload_file, bg='blue', fg='white').pack(pady=10)

# Create a label to display the sentiment result
sentiment_result = StringVar()
sentiment_label = Label(root, textvariable=sentiment_result, font=("Helvetica", 16))
sentiment_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
