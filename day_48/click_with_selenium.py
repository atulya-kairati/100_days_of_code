from selenium.webdriver.chrome.options import Options
from selenium import webdriver

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

# to keep chrome from closing automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)


driver.get(url='https://duckduckgo.com/?q=plants&t=h_&iar=images&iax=images&ia=images')
driver.implicitly_wait(10)

image = driver.find_element_by_css_selector(css_selector='.tile--img__media__i img')

print(image.get_attribute('alt'))

image.click()

# driver.quit()
