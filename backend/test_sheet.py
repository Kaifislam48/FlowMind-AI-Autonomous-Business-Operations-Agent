from services.google_sheets_service import save_lead_to_sheet

save_lead_to_sheet(
    "Kaif",
    "kaif@example.com",
    "Testing Google Sheets",
    95,
    "HOT"
)

print("Success")