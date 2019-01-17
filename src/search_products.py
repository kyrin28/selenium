# -*- coding:UTF-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir + '/bin')
driver_path = base_dir + '/bin/chromedriver'


# 初始化 chrome service
chrome_service = Service(executable_path=driver_path)
chrome_service.command_line_args()
chrome_service.start()

# 初始化 driver
driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.linkedsee.com/")

products = driver.find_elements_by_xpath("//ul[@class='drop box-1']/li/a")
print(products)

print("found " + str(len(products)) + "products")

for product in products:
    print(product.get_attribute('textContent'))

driver.quit()
chrome_service.stop()
