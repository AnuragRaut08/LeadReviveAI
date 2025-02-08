import os
import groclake

def authenticate():
    """
    Authenticate with the Groclake API using the provided API key.
    Returns a Groclake client instance.
    """
    api_key = os.getenv("GROCLAKE_API_KEY")
    if not api_key:
        raise ValueError("GROCLAKE_API_KEY environment variable not set.")
    return groclake.Client(api_key=api_key)
