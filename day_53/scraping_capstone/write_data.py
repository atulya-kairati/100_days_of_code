from selenium import webdriver


class FormFiller:

    def __init__(self):
        self.form = "https://docs.google.com/forms/d/e/1FAIpQLSd6-7WniQjO4cIHT2r3eXT7f1evutBrJJM6Mwu2TEwRNjadug/viewform?usp=sf_link"
        self.CHROME_DRIVER = "/home/atulya/PycharmProjects/pythonProject/day_53/webdrivers/chromedriver"

    def fill_form(self, data: list):
        driver = webdriver.Chrome(executable_path=self.CHROME_DRIVER)

        i = 0
        while True:
            driver.get(self.form)
            driver.implicitly_wait(20)  # if u don't wait it will throw error

            price_input = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
            link_input = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
            submit_button = driver.find_element_by_class_name(name="appsMaterialWizButtonPaperbuttonContent")

            price_input.send_keys(data[i][0])
            address_input.send_keys(data[i][1])
            link_input.send_keys(data[i][2])
            submit_button.click()

            i += 1
            if i > len(data) - 1:
                break

        driver.quit()
