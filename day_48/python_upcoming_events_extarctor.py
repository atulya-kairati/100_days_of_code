from selenium import webdriver
from pprint import pprint

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(url='https://www.python.org/')

dates = driver.find_elements_by_css_selector('.event-widget div .menu li time')
events = driver.find_elements_by_css_selector('.event-widget div .menu li a')

upcoming_events = {i: {'time': dates[i].text, 'name': events[i].text} for i in range(len(dates))}

pprint(upcoming_events)
driver.quit()
