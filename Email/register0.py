import json
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_keys_one_by_one(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

with open('config.json', 'r') as file:
    config = json.load(file)

driver = webdriver.Chrome()
driver.get(config["url"])

wait = WebDriverWait(driver, 80)
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'js-open-login')))
time.sleep(1) 
login_button.click()
time.sleep(1) 

print("okaylogin")


create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Sign in with Google')]")))
time.sleep(1) 
create_account_button.click()

print("okaysign")

email_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME,"identifier")))
send_keys_one_by_one(email_field, config["email"])



next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "identifierNext")))

next_button.click()

print("okaymail")

time.sleep(5)

