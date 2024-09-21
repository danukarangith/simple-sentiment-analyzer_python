# Sentiment Analyzer

This is a simple web application for performing sentiment analysis on text input using Flask and TextBlob. The application allows users to enter text and receive a sentiment analysis result indicating whether the text is positive, negative, or neutral. 

## Features

- Text input for sentiment analysis
- Backend powered by Flask
- Sentiment analysis using TextBlob
- User-friendly web interface with HTML and JavaScript

## Project Structure

- `app.py`: The main Flask application file that handles backend logic and routes.
- `templates/index.html`: The HTML template for the frontend user interface.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- TextBlob

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/danukarangith/sentiment-analysis-app.git
    cd sentiment-analysis-app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install flask textblob
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

### Usage

- Enter text into the textarea and click the "Analyze Text" button.
- The sentiment result will be displayed below the form.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements
tbd

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Web framework for Python
- [TextBlob](https://textblob.readthedocs.io/en/dev/) - Text processing library for Python
- [HTML](https://www.w3.org/TR/html5/) - Markup language for creating web pages

