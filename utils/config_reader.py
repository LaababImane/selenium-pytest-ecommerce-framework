import json
import os

def get_config():

    valid_username = os.environ.get("VALID_USERNAME")
    valid_password = os.environ.get("VALID_PASSWORD")

    if valid_username and valid_password:
        return {
            "base_url": "https://www.demoblaze.com",
            "valid_user": {
                "email": valid_username,
                "password": valid_password
            },
            "invalid_user": {
                "email": "invalid@example.com",
                "password": "wrongpassword"
            }
        }

    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.json")
    with open(config_path, "r") as f:
        return json.load(f)