from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

# to stop window from closing
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

driver.get('http://secure-retreat-92358.herokuapp.com')
driver.implicitly_wait(10)

fname = driver.find_element_by_name('fName')
lname = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')
button = driver.find_element_by_class_name('btn-primary')

fname.send_keys('Naughtius')
lname.send_keys('Maximus')
email.send_keys('naughty.max69420@rome.com')

button.click()

