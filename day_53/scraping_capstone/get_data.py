import requests
from bs4 import BeautifulSoup


class GetRoomData:

    def __init__(self):
        self.url = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.536739%2C%22east%22%3A-122.329919%2C%22south%22%3A37.707608%2C%22north%22%3A37.842913%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A911699%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }

    def get_data(self):
        zillow_url = "https://www.zillow.com"
        res = requests.get(url=self.url, headers=self.headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')

        prices_tags = soup.find_all(name='div', class_="list-card-price")
        address_tags = soup.find_all(name='address', class_="list-card-addr")
        link_tags = soup.select('.list-card-info a')

        prices = [price.find(text=True, recursive=False) for price in prices_tags]
        addresses = [address.getText() for address in address_tags]
        links = [link.get('href') for link in link_tags]

        fixed_links = [link if zillow_url in link else zillow_url+link for link in links]
        return list(zip(prices, addresses, fixed_links))
