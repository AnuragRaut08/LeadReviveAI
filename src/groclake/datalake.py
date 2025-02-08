from .authentication import authenticate

client = authenticate()

def store_lead_call_log(lead_id: str, conversation: str, sentiment: str):
    client.datalake.store(f"{lead_id}_call_logs", {"conversation": conversation, "sentiment": sentiment})

def retrieve_lead_history(lead_id: str):
    return client.datalake.retrieve(f"{lead_id}_call_logs")

def log_agent_performance(metrics: dict):
    client.datalake.store("agent_performance", metrics)
