import requests
from datetime import datetime

username = 'atulya'
token = "sldlkvndfnvoi9r5"
graph_name = 'g1'

# profile: https://pixe.la/@atulya

# def create_user(username, token):
#     PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
#
#     user_params = {
#         "token": token,
#         "username": username,
#         "agreeTermsOfService": "yes",
#         "notMinor": "yes",
#     }
#
#     res = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#     print(res.content)

def create_graph(id, name, unit, color='sora'):
    api = f'https://pixe.la/v1/users/{username}/graphs'
    headers = {
        'X-USER-TOKEN': token
    }
    json_data = {
        'id': id,
        'name': name,
        'unit': unit,
        'type': 'int',
        'color': color,
        'timezone': 'Asia/Kolkata'
    }
    res = requests.post(url=api, json=json_data, headers=headers)
    print(res.content)


# create_graph(id='flutter1', name='flutter_graph', unit='min')


def create_pixel(date: datetime, quantity):
    api = f'https://pixe.la/v1/users/{username}/graphs/{graph_name}'
    print(api)
    headers = {
        'X-USER-TOKEN': token
    }
    json_data = {
        "date": f"{date.year}{date.month}{date.day}",
        "quantity": quantity,
    }
    res = requests.post(url=api, json=json_data, headers=headers)
    print(res.content)


create_pixel(date=datetime.now(), quantity='5')
