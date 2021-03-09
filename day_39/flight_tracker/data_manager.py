import gspread
from oauth2client.service_account import ServiceAccountCredentials


class DataManager:

    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('sheets_auth.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open('travel_sheet')
        # sheet.add_worksheet(title='air_budget_sheet', rows=30, cols=3)
        budget_sheet = sheet.get_worksheet(0)
        col_no = budget_sheet.col_count
        # print(f'Logging data in {workout_sheet.title} from {sheet.title}')
        all_values = budget_sheet.get_all_values()
        self.budget_data = [{all_values[0][i].lower(): row[i] for i in range(col_no)} for row in all_values[1:]]
        # print(self.budget_data)

    def get_budget_data(self):
        return self.budget_data


