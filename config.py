import os
from dotenv import load_dotenv

load_dotenv()

account_id = os.getenv("ACCOUNT_ID")
api_token = os.getenv("API_TOKEN")

model_name = os.getenv("MODEL_NAME")
url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model_name}"
