from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

from NewsFetch import get_german_news

api_key = os.getenv("API_KEY")

news_list = get_german_news(api_key)

print("Loading AI model... (this may take a minute the first time)")
ner_model = pipeline(
    "ner", 
    model="Davlan/bert-base-multilingual-cased-ner-hrl", ##Using a BERT-based multilingual model from Hugging Face
    aggregation_strategy="simple"
)
def extract_companies(articles):
    structured_results = []
    
    for art in articles:
        text = art['title']
        entities = ner_model(text)
        companies = [ent['word'] for ent in entities if ent['entity_group'] == 'ORG']
        
        structured_results.append({
            "title": text,
            "companies": list(set(companies)), 
            "url": art['url']
        })

    usefulResults = [
        res for res in structured_results
        if res['companies'] and res['companies'] != ["Unknown Company"]
    ]
    
    return usefulResults

if __name__ == "__main__":
    results = extract_companies(news_list)
    for res in results:
        print(f"Title: {res['title']}")
        print(f"Companies: {', '.join(res['companies']) if res['companies'] else 'None'}")
        print(f"Link: {res['url']}\n")
