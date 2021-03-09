from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

# to keep chrome from closing automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

driver.get('https://google.com')

search_bar = driver.find_element_by_name('q')  # every input has a name

# search_bar.send_keys('Biggus Dickus\n')  # this works fine
search_bar.send_keys('Sillius Soddos')
search_bar.send_keys(Keys.ENTER)  # but this is better
