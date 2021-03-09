from selenium.webdriver.chrome.options import Options
from selenium import webdriver

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

# to keep chrome from closing automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

driver.get('https://google.com')

lucky = driver.find_element_by_link_text("Images")

lucky.click()
