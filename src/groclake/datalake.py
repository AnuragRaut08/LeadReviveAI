from .authentication import authenticate

client = authenticate()

def store_lead_call_log(lead_id: str, conversation: str, sentiment: str):
    """
    Store lead call logs using Groclake's Datalake.
    """
    client.datalake.store(f"{lead_id}_call_logs", {
        "conversation": conversation,
        "sentiment": sentiment
    })

def retrieve_lead_history(lead_id: str) -> dict:
    """
    Retrieve past interactions from Groclake's Datalake.
    """
    return client.datalake.retrieve(f"{lead_id}_call_logs")

def log_agent_performance(metrics: dict):
    """
    Log AI agent performance metrics in Groclake's Datalake.
    """
    client.datalake.store("agent_performance", metrics)
