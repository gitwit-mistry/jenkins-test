import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

def read_secret_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Get the secret file path from the environment variable
secret_file_path = os.environ.get('SECRET_FILE')

def read_google_sheet():
    # Replace 'YOUR_SERVICE_ACCOUNT_KEY.json' with the path to your service account JSON file
    credentials = ServiceAccountCredentials.from_json_keyfile_name(secret_file_path, ['https://www.googleapis.com/auth/spreadsheets'])

    # Replace 'YOUR_GOOGLE_SHEET_URL' with the URL of your Google Sheet
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1z46OmoTLXqNyCgOllWZ38s0DRi_83WKs6hOPeB2xIQU/edit#gid=0')

    # Access a specific worksheet by its title
    worksheet = sheet.worksheet('Vitamins')

    # Read data from the worksheet
    data = worksheet.get_all_values()
    return data

if __name__ == "__main__":
    sheet_data = read_google_sheet()
    print(sheet_data)


# # Read and parse the JSON data from the secret file
# if secret_file_path:
#     secret_data = read_secret_json_file(secret_file_path)
#     # Now you can use the secret_data dictionary in your Python script as needed
#     print(secret_data)
# else:
#     print("Secret file path not found. Make sure you set the SECRET_FILE environment variable.")
