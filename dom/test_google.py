import unittest
from selenium import webdriver
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../chromedriver/chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')
        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
