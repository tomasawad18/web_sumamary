import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

# ==============================
# Load البيئة
# ==============================
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY or not API_KEY.startswith("sk-or-"):
    raise ValueError("❌ Invalid or missing OpenRouter API Key. Check your .env file.")

# ==============================w
# Initialize OpenRouter Client
# ==============================
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "GenAI Website Summarizer"
    }
)

# ==============================
# Fetch Website Content
# ==============================
def fetch_website_content(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # إزالة السكربتات
        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        if not text:
            raise ValueError("No readable content found on the page.")

        return text[:5000]  # limit tokens

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch website: {e}")
        return None
    except Exception as e:
        print(f"[ERROR] Parsing failed: {e}")
        return None


# ==============================
# Analyze with LLM
# ==============================
def analyze_with_llm(content):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4.1-mini",  # 🔥 best balance
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI that summarizes and explains website content clearly."
                },
                {
                    "role": "user",
                    "content": f"Summarize this content in a clear and structured way:\n\n{content}"
                }
            ],
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"[ERROR] LLM processing failed: {e}")
        return None


# ==============================
# Main App
# ==============================
def main():
    try:
        url = input("Enter website URL: ").strip()

        if not url.startswith("http"):
            raise ValueError("URL must start with http or https.")

        print("\n[INFO] Fetching website content...")
        content = fetch_website_content(url)

        if not content:
            print("[ERROR] No content retrieved.")
            return

        print("[INFO] Sending to LLM...")
        result = analyze_with_llm(content)

        if result:
            print("\n===== AI SUMMARY =====\n")
            print(result)
        else:
            print("[ERROR] Failed to generate summary.")

    except ValueError as ve:
        print(f"[INPUT ERROR] {ve}")

    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user.")

    except Exception as e:
        print(f"[UNEXPECTED ERROR] {e}")


# ==============================
# Run
# ==============================
if __name__ == "__main__":
    main()

###
