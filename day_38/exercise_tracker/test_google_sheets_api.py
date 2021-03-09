import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets_auth.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('workout_data')

# get the first sheet of the Spreadsheet
#sheet_instance = sheet.get_worksheet(0)

# sheet.add_worksheet(title='workout_lgs', cols=3, rows=20)
workout_sheet = sheet.get_worksheet(0)
workout_sheet.append_row(['asfdsf', 'wefwef', 3.4])

# val = sheet_instance.get_all_values()
#
# print(val)