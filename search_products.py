# -*- coding:UTF-8 -*-

from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.linkedsee.com/")

# search_field = driver.find_element_by_name('q')
# search_field.clear()
#
# search_field.send_keys('phone')
# search_field.submit()


products = driver.find_elements_by_xpath("//ul[@class='drop box-1']/li/a")
print(driver.find_element_by_css_selector("#xh-highlight").is_displayed())
print(products)

print("found " + str(len(products)) + "products")

for product in products:
    print(product.get_attribute('textContent'))

driver.quit()
