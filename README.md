# Google Sheets CSV Automation with Python

This script automatically uploads CSV data to a Google Sheet using Python, the Google Sheets API, and a Service Account. It's perfect for automating reports, syncing sales data, or logging inventory from exports.

---

## 🚀 Features
- Uploads data from a `.csv` file into Google Sheets
- Automatically clears old data and updates with fresh content
- Adds a timestamp to each row (optional)
- Simple to set up and run locally

---

## 🧰 Technologies Used
- Python 3
- `gspread` (Google Sheets API wrapper)
- `oauth2client`
- `pandas`

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/trentenfleetham/trentenfleetham/blob/0533b8fc25b4ff2c60c35a4fc282570011de327c/Upwork/CSVtoSheet.py
cd CSVtoSheet