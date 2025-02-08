import pytest
from unittest.mock import MagicMock
from src.groclake.datalake import store_lead_call_log, retrieve_lead_history, log_agent_performance

@pytest.fixture
def mock_client(mocker):
    client = MagicMock()
    mocker.patch("src.groclake.authentication.authenticate", return_value=client)
    return client

def test_store_lead_call_log(mock_client):
    store_lead_call_log("lead_123", "Test conversation", "Positive")
    mock_client.datalake.store.assert_called_with("lead_123_call_logs", {
        "conversation": "Test conversation",
        "sentiment": "Positive"
    })

def test_retrieve_lead_history(mock_client):
    mock_client.datalake.retrieve.return_value = {"conversation": "Test conversation", "sentiment": "Positive"}
    assert retrieve_lead_history("lead_123") == {"conversation": "Test conversation", "sentiment": "Positive"}

def test_log_agent_performance(mock_client):
    log_agent_performance({"success_rate": 90})
    mock_client.datalake.store.assert_called_with("agent_performance", {"success_rate": 90})
