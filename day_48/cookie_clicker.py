from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

chrome_option = Options()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_option)

driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')

for _ in range(10000):
    cookie.click()
