import pytest
from unittest.mock import MagicMock
from src.groclake.vectorlake import create_lead_embedding, get_similar_leads

@pytest.fixture
def mock_client(mocker):
    client = MagicMock()
    mocker.patch("src.groclake.authentication.authenticate", return_value=client)
    return client

def test_create_lead_embedding(mock_client):
    mock_client.vectorlake.create_embedding.return_value = {"embedding": [0.1, 0.2, 0.3]}
    assert create_lead_embedding({"name": "John Doe"}) == {"embedding": [0.1, 0.2, 0.3]}

def test_get_similar_leads(mock_client):
    mock_client.vectorlake.query_embedding.return_value = ["Lead1", "Lead2"]
    assert get_similar_leads("John Doe", 2) == ["Lead1", "Lead2"]
