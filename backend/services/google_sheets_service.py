import gspread
import re
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file(
    "credentials/google-credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

SHEET_ID = "1WiZgbL8EWlL01o02oFSbz4GDKetc_Iw2ZYgEkECgj3w"


def extract_score_category(analysis):
    score_match = re.search(r"Score:\s*(\d+)", analysis)
    category_match = re.search(
        r"Category:\s*(HOT|WARM|COLD)",
        analysis,
        re.IGNORECASE
    )

    score = score_match.group(1) if score_match else "N/A"
    category = (
        category_match.group(1)
        if category_match
        else "UNKNOWN"
    )

    return score, category


def save_lead_to_sheet(name, email, message, analysis):

    score, category = extract_score_category(
        analysis
    )

    sheet = client.open_by_key(
        SHEET_ID
    ).sheet1

    sheet.append_row([
        name,
        email,
        message,
        score,
        category
    ])