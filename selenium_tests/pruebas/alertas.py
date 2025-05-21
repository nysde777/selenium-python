from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/javascript_alerts")
alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_button.click()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert_text = alert.text
print("Texto: ", alert_text)
alert.accept()


confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()
alert = driver.switch_to.alert
alert.dismiss()


confirm_prompt = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
confirm_prompt.click()
alert = driver.switch_to.alert
alert.send_keys("texto para la alerta desde selenium")
alert.accept()

result = driver.find_element(By.ID, "result").text
print("Resultado: ", result)
time.sleep(3)

driver.quit()