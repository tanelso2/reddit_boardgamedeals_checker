import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_list_of_games_from_sheet():
    scope = ['https://spreadsheets.google.com/feeds']
    access_key = os.path.join(config_dir, "access_key.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(access_key, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open("Board Games Wishlist")
    records = spreadsheet.worksheet("Sheet1").get_all_records()
    return [ a['Name'].lower() for a in records ]
