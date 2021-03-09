from datetime import datetime, timedelta

import requests


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    API_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'
    API_KEY = 'XfQlcbjmM9lsBMvKlyyebzpK7seg89aA'

    def __init__(self):
        now = datetime.now()
        six_months_form_now = now + timedelta(days=1)
        self.date_from = now.strftime('%d/%m/%Y')
        self.date_to = six_months_form_now.strftime('%d/%m/%Y')

    def get_budget_flights(self, fly_to, budget, fly_from='DEL'):
        headers = {
            'apikey': FlightSearch.API_KEY
        }
        query = {
            'fly_to': fly_to,
            'fly_from': fly_from,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'curr': 'INR',
            'price_to': budget,
        }
        res = requests.get(url=FlightSearch.API_ENDPOINT, params=query, headers=headers)
        res.raise_for_status()
        flights: list = res.json()['data']
        # print(flights)
        if len(flights) == 0:
            return
        info = f'{len(flights)} flight found for {flights[0]["cityFrom"]} to {flights[0]["cityTo"]}\n\n'
        for flight in flights:
            info += f'{flight["price"]}INR + bag price as in: {flight["bags_price"]}\nBooking Link:\n{flight["deep_link"]}\n\n'

        return info


if __name__ == '__main__':
    fs = FlightSearch()
    fs.get_budget_flights(fly_to='BOM', budget=4400)
