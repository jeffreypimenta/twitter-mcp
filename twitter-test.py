
import twikit
import os
from pathlib import Path
import logging
from typing import Optional, List
import time

USERNAME = 'JeffreyPimenta'
PHONE_NUMBER = '9167159151'
PASSWORD = 'Viv@Selec@07'
USER_AGENT = user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
COOKIES_PATH = Path.home() / 'Documents' / 'mcp' / 'cookies.json'

logger = logging.getLogger(__name__)

RATE_LIMITS = {}
RATE_LIMIT_WINDOW = 15 * 60

def get_twitter_client():
    client = twikit.Client('en-us', user_agent=USER_AGENT)

    if COOKIES_PATH.exists():
        client.load_cookies(COOKIES_PATH)
    else:
        try:
            client.login(
                auth_info_1=USERNAME,
                auth_info_2=PHONE_NUMBER,
                password=PASSWORD
            )
        except Exception as e:
            logger.error(f"Failed to login:{e}")
            raise

    return client.user()

def check_rate_limit(endpoint: str) -> bool:
    """Check if we're within rate limits for a given endpoint."""
    now = time.time()
    if endpoint not in RATE_LIMITS:
        RATE_LIMITS[endpoint] = []

    # Remove old timestamps
    RATE_LIMITS[endpoint] = [t for t in RATE_LIMITS[endpoint] if now - t < RATE_LIMIT_WINDOW]

    # Check limits based on endpoint
    if endpoint == 'tweet':
        return len(RATE_LIMITS[endpoint]) < 300  # 300 tweets per 15 minutes
    elif endpoint == 'dm':
        return len(RATE_LIMITS[endpoint]) < 1000  # 1000 DMs per 15 minutes
    return True



if __name__ == "__main__":
    print(get_twitter_client())
