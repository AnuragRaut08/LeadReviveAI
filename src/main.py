from groclake.modellake import analyze_sentiment
from utils.logger import setup_logger

def main():
    logger = setup_logger('LeadReviveAI', 'leadreviveai.log')
    sample_text = "Hello, I'm interested in your product."
    sentiment_score, sentiment_label = analyze_sentiment(sample_text)
    logger.info(f"Sentiment: {sentiment_label} (Score: {sentiment_score})")

if __name__ == "__main__":
    main()
