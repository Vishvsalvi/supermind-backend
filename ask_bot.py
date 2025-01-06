# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token

import requests
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "73ed6dad-e50e-4c33-b0f2-96c64c5a093c"
FLOW_ID = "4147aab8-c8ab-4f42-aecb-35edea9a0031"
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")

def ask_chat_bot(question):
    TWEAKS = {"TextInput-ioxSO": {"input_value": question}}
    
    return run_flow_ask_chat_bot(
        "", tweaks=TWEAKS, application_token=APPLICATION_TOKEN
    )

def run_flow_ask_chat_bot(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/ask-bot"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()  # Ensure we raise an error for bad responses
    return response.json()["outputs"][0]["outputs"][0]["results"]["message"]["text"]

