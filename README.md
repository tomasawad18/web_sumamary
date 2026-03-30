GenAI Website Summarizer

A powerful CLI-based AI tool that fetches website content and generates a clear, structured summary using LLMs via OpenRouter.

Overview

GenAI Website Summarizer is a Python application that allows you to:

Extract readable content from any website
Clean and preprocess HTML (remove scripts, styles, etc.)
Generate intelligent summaries using an AI model
Get fast, structured insights from long web pages

This tool is ideal for developers, researchers, and anyone who wants to quickly understand online content without reading entire pages.

How It Works
The app fetches website content using requests
Parses and cleans HTML using BeautifulSoup
Sends processed text to an LLM via OpenRouter
Returns a concise and structured summary
Tech Stack
Python 3.x
requests
beautifulsoup4
python-dotenv
openai (used with OpenRouter API)
Installation
# Clone the repository
git clone https://github.com/tomasawad18/genai-website-summarizer.git

# Navigate into the project
cd genai-website-summarizer

# Install dependencies
pip install -r requirements.txt
Environment Variables (IMPORTANT)

This project requires an OpenRouter API key.

You must create a .env file in the root directory and add your API key:

OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxx

Important notes:

Your key must start with sk-or-
Never share your .env file or commit it to GitHub
Add .env to your .gitignore
Usage
python app.py

Then enter a website URL:

Enter website URL: https://example.com
Example Output
[INFO] Fetching website content...
[INFO] Sending to LLM...

===== AI SUMMARY =====

This website discusses...
Error Handling

The app includes error handling for:

Invalid or missing API keys
Network failures
Unreadable or empty web pages
Invalid URLs
Features
Clean and structured summaries
Token-limited processing for efficiency
Simple CLI interface
Modular and extensible codebase
Future Improvements
Support for multiple languages
Web-based UI
Export summaries (PDF / Markdown)
Keyword extraction and insights
Contributing

Contributions are welcome. You can:

Fork the repository
Create a new branch
Submit a pull request
