from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
driver.execute_script("arguments[0].click();", add_to_cart_button)

product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name")
driver.execute_script("arguments[0].innerText= 'Producto Modificado';", product_name)

modified_text = product_name.text
print("Texto: ", modified_text)
time.sleep(5)
