from langchain_ollama import OllamaLLM
from extract_entities import extract_companies, news_list


#"I use Ollama to run LLMs locally. This ensures that sensitive supply c
# hain news or company data never leaves our private servers, 
# which is essential for GDPR compliance."



# 1. Connect to your local AI
llm = OllamaLLM(model="llama3.2:3b")

def analyze_supply_chain_risk(company_name, news_titles):
    # This is called 'Prompt Engineering'
    # We are giving the AI a specific 'Role' and 'Context'
    context = "\n".join(news_titles)
    
    prompt = f"""
    You are a Senior Supply Chain Risk Analyst in Germany.
    
    CONTEXT (Latest News):
    {context}
    
    TASK:
    Based ONLY on the news above, what is the potential risk to {company_name}? 
    If the news doesn't mention a specific risk, say "No immediate risk detected."
    
    FORMAT:
    - Risk Level: (Low/Medium/High)
    - Summary: (1 sentence)
    """

    response = llm.invoke(prompt)
    return response

if __name__ == "__main__":
    # 2. Extract companies from news
    structured_results = extract_companies(news_list)
    
    # 3. Analyze risk for each company
    for res in structured_results:
        company_name = res['companies'][0] if res['companies'] else "Unknown Company"
        news_titles = [res['title']]
        
        print(f"Analyzing risk for {company_name}...")
        risk_analysis = analyze_supply_chain_risk(company_name, news_titles)
        print(f"Risk Analysis for {company_name}:\n{risk_analysis}\n{'-'*50}\n")