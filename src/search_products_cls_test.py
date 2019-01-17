# -*- coding:UTF-8 -*-

import os
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir + '/bin')
driver_path = base_dir + '/bin/chromedriver'


class ProductTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化 chrome service
        cls.chrome_service = Service(executable_path=driver_path)
        cls.chrome_service.command_line_args()
        cls.chrome_service.start()

        # 初始化 driver
        cls.driver = webdriver.Chrome(driver_path)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("http://www.linkedsee.com/")

    def test_product_num(self):
        products = self.driver.find_elements_by_xpath("//ul[@class='drop box-1']/li/a")
        print("found " + str(len(products)) + " products")

        for product in products:
            print(product.get_attribute('textContent'))
        self.assertEqual(3, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.chrome_service.stop()


if __name__ == "__main__":
    unittest.main()
