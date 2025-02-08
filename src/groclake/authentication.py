import groclake
from src.config import GROCLAKE_API_KEY

def authenticate():
    """
    Authenticate with the Groclake API.
    Returns a Groclake client instance.
    """
    if not GROCLAKE_API_KEY:
        raise ValueError("GROCLAKE_API_KEY environment variable not set.")
    return groclake.Client(api_key=GROCLAKE_API_KEY)
