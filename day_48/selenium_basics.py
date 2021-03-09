from selenium import webdriver

CHROME_DRIVER_PATH = '/home/atulya/PycharmProjects/pythonProject/day_48/webdrivers/chromedriver'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(
    'https://www.amazon.in/India-Raspberry-Official-Heatsink-Ethernet/dp/B07XSJ64ZY/ref=sr_1_1_sspa?crid=2CHP1HGOWOFME&dchild=1&keywords=raspberry+pi&qid=1610356010&sprefix=rasp%2Caps%2C491&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFXVlRWV1ZBUUE1OVgmZW5jcnlwdGVkSWQ9QTA0ODk5MjYxOEdYWjVLTVIyOVpNJmVuY3J5cHRlZEFkSWQ9QTA3ODIyODIxNlRCTFBDOFZWOTk3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')

price = driver.find_element_by_id(id_="priceblock_saleprice").text

img = driver.find_element_by_xpath(xpath='//*[@id="landingImage"]').get_attribute('src')

# using css selectors to find all related products on the page
product = driver.find_elements_by_css_selector('.a-carousel-card div .a-link-normal')[0].get_attribute('href')

print(product)

print(img)

print(price)

driver.quit()

