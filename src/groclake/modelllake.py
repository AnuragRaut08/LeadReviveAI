from .authentication import authenticate

client = authenticate()

def speech_to_text(audio_file: str):
    response = client.modellake.speech_to_text(audio_file=audio_file)
    return response.get("transcript", "")

def chat_with_ai(prompt: str):
    response = client.modellake.chat(prompt=prompt)
    return response.get("reply", "")

def translate_text(text: str, target_language: str):
    response = client.modellake.translate(text=text, target_language=target_language)
    return response.get("translated_text", "")

def analyze_sentiment(text: str):
    response = client.modellake.sentiment_analysis(text=text)
    return response.get("score", 0), response.get("label", "Neutral")
