from selenium import webdriver

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]').text

print(article_count)
