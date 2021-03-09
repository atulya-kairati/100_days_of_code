import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

"sheet is stored in quotebot80"


def update_logs(all_exercise_list):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('sheets_auth.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('workout_data')
    workout_sheet = sheet.get_worksheet(0)
    print(f'Logging data in {workout_sheet.title} from {sheet.title}')
    workout_sheet.append_rows(values=all_exercise_list)


def get_exercises(activity: str):
    nutrionix_api = 'https://trackapi.nutritionix.com/v2/natural/exercise'

    headers = {
        'x-app-id': 'b0fac131',
        'x-app-key': '6b1f66bfb079b7e13d274e4a53044499',
    }

    query = {
        "query": activity,
        "gender": "male",
        "weight_kg": 55,
        "height_cm": 170,
        "age": 22
    }

    res = requests.post(url=nutrionix_api, headers=headers, json=query)
    exercises = res.json()['exercises']
    return [[e["user_input"], e["duration_min"], e["nf_calories"]] for e in exercises]


user_input = input('Tell me what you did: ')

exercise_list = get_exercises(user_input)
update_logs(exercise_list)

