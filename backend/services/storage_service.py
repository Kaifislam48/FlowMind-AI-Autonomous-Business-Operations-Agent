import json
import os

FILE_PATH = "data/leads.json"

def save_lead(data):

    os.makedirs("data", exist_ok=True)

    leads = []

    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as f:
                leads = json.load(f)

            if not isinstance(leads, list):
                leads = []

        except:
            leads = []

    leads.append(data)

    with open(FILE_PATH, "w") as f:
        json.dump(leads, f, indent=4)