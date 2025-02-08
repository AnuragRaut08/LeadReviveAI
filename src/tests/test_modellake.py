import pytest
from unittest.mock import MagicMock
from src.groclake.modellake import speech_to_text, chat_with_ai, translate_text, analyze_sentiment

@pytest.fixture
def mock_client(mocker):
    client = MagicMock()
    mocker.patch("src.groclake.authentication.authenticate", return_value=client)
    return client

def test_speech_to_text(mock_client):
    mock_client.modellake.speech_to_text.return_value = {"transcript": "Hello world"}
    assert speech_to_text("dummy.wav") == "Hello world"

def test_chat_with_ai(mock_client):
    mock_client.modellake.chat.return_value = {"reply": "Hello, how can I help you?"}
    assert chat_with_ai("Hi") == "Hello, how can I help you?"

def test_translate_text(mock_client):
    mock_client.modellake.translate.return_value = {"translated_text": "Hola"}
    assert translate_text("Hello", "es") == "Hola"

def test_analyze_sentiment(mock_client):
    mock_client.modellake.sentiment_analysis.return_value = {"score": 0.9, "label": "Positive"}
    assert analyze_sentiment("I love this!")[1] == "Positive"
