from .authentication import authenticate

client = authenticate()

def speech_to_text(audio_file: str) -> str:
    """
    Convert speech to text using Groclake's Modellake.
    """
    response = client.modellake.speech_to_text(audio_file=audio_file)
    return response.get("transcript", "")

def chat_with_ai(prompt: str) -> str:
    """
    Get AI-generated response using Groclake's Modellake.
    """
    response = client.modellake.chat(prompt=prompt)
    return response.get("reply", "")

def translate_text(text: str, target_language: str) -> str:
    """
    Translate text to the target language using Groclake's Modellake.
    """
    response = client.modellake.translate(text=text, target_language=target_language)
    return response.get("translated_text", "")

def analyze_sentiment(text: str) -> tuple:
    """
    Perform sentiment analysis on the provided text using Groclake's Modellake.
    Returns a tuple of sentiment score and label.
    """
    response = client.modellake.sentiment_analysis(text=text)
    return response.get("score", 0), response.get("label", "Neutral")
