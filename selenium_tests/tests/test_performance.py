import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.config import load_config
import time

config = load_config()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

start_time = time.time()
driver.get(config["base_url"])
loginPage = LoginPage(driver)

loginPage.set_username(config["valid_user"])
loginPage.set_password(config["valid_password"])
loginPage.click_login()
end_time = time.time()
load_time = end_time - start_time
print(f"tiempo de carga de login:{load_time:2f} segundos")
driver.quit()