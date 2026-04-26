# German Industrial Risk Intelligence Hub

An AI-powered web dashboard for automated supply chain risk monitoring in the German Mittelstand sector. This application fetches multilingual news, extracts company entities using advanced NLP, and analyzes potential risks using local large language models.

##  Features

- **Multilingual News Fetching**: Retrieves relevant news in German and English for comprehensive coverage
- **Named Entity Recognition**: Uses BERT-based multilingual model to extract company names from news headlines
- **Risk Analysis**: Leverages Llama 3.2 via Ollama for intelligent supply chain risk assessment
- **Bilingual Interface**: Supports English and German user interfaces
- **Real-time Processing**: Provides instant risk reports based on latest news data
- **Privacy-Focused**: Runs entirely locally with no data sent to external servers

##  Tech Stack

- **Frontend**: Streamlit
- **AI/ML**: Transformers, PyTorch, LangChain-Ollama
- **APIs**: NewsAPI
- **Languages**: Python 3.8+
- **Environment**: Virtual environments

##  Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- NewsAPI key (free tier available)

##  Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/garima3012/NewsFetchProject.git
   cd NewsFetchProject
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your NewsAPI key: `API_KEY=your_api_key_here`

5. **Install and run Ollama**
   ```bash
   # Install Ollama from https://ollama.ai
   ollama pull llama3.2:3b
   ollama serve
   ```

## Usage

1. **Start the application**
   ```bash
   streamlit run dashboard.py
   ```

2. **Access the dashboard**
   - Open your browser to `http://localhost:8501`
   - Select language (English/Deutsch) in the sidebar
   - Enter your NewsAPI key
   - Input a target company (e.g., BMW)
   - Click "Generate Risk Report"

3. **View results**
   - Real-time analysis status
   - Extracted companies from news
   - Detailed risk assessment
   - Source news articles

## Project Structure

```
NewsFetchProject/
├── dashboard.py          # Main Streamlit application
├── NewsFetch.py          # News API integration
├── extract_entities.py   # NER and entity extraction
├── risk_analyst.py       # LLM risk analysis
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Garima Kumari**  
- GitHub: [@garima3012](https://github.com/garima3012)
- LinkedIn: [Garima Kumari](https://www.linkedin.com/in/garima-kumari-0840731a7)

## Acknowledgments

- [NewsAPI](https://newsapi.org/) for news data
- [Hugging Face](https://huggingface.co/) for BERT models
- [Ollama](https://ollama.ai/) for local LLM hosting
- [Streamlit](https://streamlit.io/) for the web framework

--