from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.ID, "shopping_cart_container").click()

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("Лилит")
driver.find_element(By.ID, "last-name").send_keys("Акиншина")
driver.find_element(By.ID, "postal-code").send_keys("333666")

driver.find_element(By.ID, "continue").click()

total_price = driver.find_element(By.CLASS_NAME, 'summary_total_label')

driver.quit()

total = total_price.text.strip().replace("Total: $", "")
excepted_total = "58.29"
assert total == excepted_total
print("Итого $58.29")
