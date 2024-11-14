import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import time
import traceback

# Configuration
CREDENTIALS_FILE = '< Put your path to the json file >'
SHEET_ID = ''
CSV_PATH = 'Put your path to the csv file'


def upload_csv_to_google_sheet(csv_path, sheet_id, credentials_file):
    try:
        # Set up the credentials and authorize the client
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(creds)

        # Open the Google Sheet using the Sheet ID
        print(f"Opening the Google Sheet with ID: {sheet_id}")
        sheet = client.open_by_key(sheet_id).sheet1

        # Read the CSV file
        print(f"Reading the CSV file: {csv_path}")
        with open(csv_path, 'r') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        # Clear existing content in the sheet
        print("Clearing the sheet...")
        sheet.clear()

        # Upload data to the Google Sheet using append_rows (batch insertion)
        print("Uploading data to the Google Sheet...")
        sheet.append_rows(data, value_input_option='RAW')
        
        print("Data uploaded successfully to Google Sheet.")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

# Usage
upload_csv_to_google_sheet(CSV_PATH, SHEET_ID, CREDENTIALS_FILE)
