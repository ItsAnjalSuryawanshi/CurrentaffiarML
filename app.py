rom flask import Flask, request, jsonify
from newspaper import Article
import nltk
from nltk.tokenize import sent_tokenize

# Initialize Flask app
app = Flask(__name__)

# Download NLTK tokenizer (first time use)
nltk.download('punkt')

def summarize_news(url):
    # Extract the article
    article = Article(url)
    article.download()
    article.parse()

    # Tokenize the article into sentences
    sentences = sent_tokenize(article.text)

    # For simplicity, we will take the first 3 sentences as summary
    summary = " ".join(sentences[:3])
    return summary

@app.route('/')
def home():
    return "Welcome to the News Summarizer API!"

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "Please provide a news URL"}), 400
    
    summary = summarize_news(url)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
