import requests
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("API_KEY")
if api_key:
    print("API key loaded successfully.")
else:
    print(f"Failed to load API key from {env_path}. Please check your .env file.")

def get_german_news(api_key):
    url="https://newsapi.org/v2/everything"
    query_params={
        "q": 'Manufacturing OR Automotive OR "Supply Chain"',
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 40,
        "apiKey": api_key
    }
    try:
        response=requests.get(url, params=query_params)
        response.raise_for_status()
        data=response.json()
        articles = data.get("articles", [])

        # Print the results to see what we got
        print(f"--- Found {len(articles)} articles ---\n")
        for i, art in enumerate(articles, 1):
            print(f"{i}. {art['title']}")
            print(f"   Source: {art['source']['name']}")
            print(f"   Link: {art['url']}\n")
            
        return articles

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_german_news(api_key)


