import time
from datetime import datetime, timedelta
import geopy.distance
import requests

SUN_API = r'https://api.sunrise-sunset.org/json'
ISS_API = r'http://api.open-notify.org/iss-now.json'
MY_LAT = 27.4307
MY_LNG = 82.1805


def get_separation(coord1: tuple, coord2: tuple):
    return geopy.distance.distance(coord1, coord2).km


def get_iss_loc():
    response = requests.get(url=ISS_API)
    response.raise_for_status()
    res_json = response.json()
    return {key: float(value) for key, value in res_json['iss_position'].items()}


def is_dark():
    response = requests.get(url=SUN_API, params={'lat': MY_LAT, 'lng': MY_LNG, 'formatted': 0})
    response.raise_for_status()
    res_json = response.json()
    sunrise = [int(x) for x in res_json['results']['sunrise'].split('T')[1].split('+')[0].split(':')]
    sunset = [int(x) for x in res_json['results']['sunset'].split('T')[1].split('+')[0].split(':')]
    date = [int(x) for x in res_json['results']['sunrise'].split('T')[0].split('-')]
    date.reverse()
    sunrise_utc = datetime(year=date[-1], month=date[1], day=date[0], hour=sunrise[0], minute=sunrise[1], second=sunrise[2])
    sunset_utc = datetime(year=date[-1], month=date[1], day=date[0], hour=sunset[0], minute=sunset[1], second=sunset[2])
    sunrise_local = sunrise_utc + timedelta(seconds=abs(time.timezone))
    sunset_local = sunset_utc + timedelta(seconds=abs(time.timezone))
    # print(sunrise_local)
    # print(sunset_local)
    # print(datetime.now())
    return not sunrise_local < datetime.now() < sunset_local


def track_iss():
    iss_loc = get_iss_loc()
    iss_lat, iss_lng = iss_loc['latitude'], iss_loc['longitude']
    separation = get_separation(coord1=(MY_LAT, MY_LNG), coord2=(iss_lat, iss_lng))
    print(f'Distance between you and ISS is {separation} Km')
    if separation > 50:
        print('ISS is far away, try later.')
        return
    else:
        print('Look up :)')
        print(f'ISS is at:\nLatitude: {iss_lat} and Longitude: {iss_lng}\n')
        time.sleep(10)
        track_iss()


if is_dark():
    track_iss()
else:
    print('Not Dark, ISS won\'t be visible')
