from time import sleep
import unittest
from selenium import webdriver


class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver/chromedriver.exe')
        driver = self.driver
        driver.get('https://www.mercadolibre.com/')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CL')
        country.click()
        sleep(3)

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 5')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_xpath(
            '//*[@id="root-app"]/div/div/aside/section/div[8]/ul/li[1]/a')
        # location.click() --> se modifica debido a un error
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element_by_xpath(
            '//*[@id="root-app"]/div/div/aside/section[2]/div[3]/ul/li[1]/a')
        condition.click()
        sleep(3)

        order_menu = driver.find_element_by_class_name(
            'andes-dropdown__display-values')
        order_menu.click()
        higher_price = driver.find_element_by_css_selector(
            '#andes-dropdown-más-relevantes-list-option-price_desc')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            prices.append(article_price)

        print(articles, prices)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
