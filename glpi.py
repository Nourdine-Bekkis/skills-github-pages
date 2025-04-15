
import requests
import os

def creer_ticket_glpi(description, user_email):
    headers = {
        "App-Token": os.getenv("GLPI_APP_TOKEN"),
        "Authorization": f"user_token {os.getenv('GLPI_USER_TOKEN')}"
    }
    data = {
        "input": {
            "name": "Ticket via SupportBotGPT",
            "content": description,
            "email": user_email,
            "priority": 3
        }
    }
    url = os.getenv("GLPI_API_URL", "https://votre.glpi.fr/apirest.php/Ticket")
    response = requests.post(url, json=data, headers=headers)
    return response.json()
