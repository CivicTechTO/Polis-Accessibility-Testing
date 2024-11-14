# Accessibility-Testing
## Set Up Environment
the script depends on the packages:
- Install Python3 & pip
- The commands to install through terminal
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
you also need to install libraries `gspread` before running the script.
you can install by these commands:
```bash
pip install gspread oauth2client
```
you also need to install a tool `lighthouse` before running the script.
you can install by these commands:
```bash
brew install node
```
```bash
npm install -g lighthouse
```
```bash
lighthouse 'url'
```

## Link to the Spreadsheet
- Make sure to log in througyh the service account
- The Spreadsheet has 3 sheets for the test results of the priority pages (Homepgage, Participation Page, and Report Page)
- https://docs.google.com/spreadsheets/d/1JXuXckkMHYdU8BmTRpWBOVHUKv5YQC5Wg6dBjtkJmLY/edit?usp=sharing

## Setup
- Go to Google Cloud Console
- Enable the Google Sheets API (default: it's always on)
- Download the credentials.json file from IAM Page
- In `upload2googlesheets.py`, there are 3 config you need to set before running the script
- `CREDENTIALS_FILE`: The path to the json file downloaded from Google Cloud Console (IAM page)
- `SHEET_ID`: copy it from the url to the Google sheet you are writing to
- `CSV_PATH`: the path to the output of `convert2CSV.py`

### Run the Script
```bash
python3 upload2googlesheets.py
```

## Automate the Script
```bash
crontab -e
```
```bash
0 2 * * * /path/to/venv/bin/python3 /path/to/upload2googlesheets.py
```
The test has already been automated to run by 2 AM every day

### Verify
- Open the Google Sheet to check the uploaded data.


