import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

# Setup authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("./credentials.json", scope)
client = gspread.authorize(creds)

# Open your sheet
spreadsheet = client.open("Sales Tracker")  # Change to your Sheet name
sheet = spreadsheet.sheet1

# Load your CSV (or any DataFrame)
df = pd.read_csv("sales_data.csv")  # Replace with your CSV file path

# Optional: Add a timestamp row
df['Upload Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Clear existing sheet contents
sheet.clear()

# Set headers
sheet.append_row(df.columns.tolist())

# Write data rows
for row in df.values.tolist():
    sheet.append_row(row)

print("Google Sheet updated successfully!")
