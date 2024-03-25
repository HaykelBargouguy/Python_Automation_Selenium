from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json

def send_keys_one_by_one(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

with open('config.json', 'r') as file:
    config = json.load(file)

driver = webdriver.Chrome()
driver.get(config["url"])

wait = WebDriverWait(driver, 20)

# Wait for the entire page to load
time.sleep(5)

wait = WebDriverWait(driver, 20)
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'js-open-login')))
time.sleep(3) 
login_button.click()
time.sleep(3) 

try:
    reject_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    time.sleep(3) 
    reject_cookies_button.click()
except Exception as e:
    print("Pas de boîte de dialogue des cookies à fermer.")

create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Sign in with Google')]")))
time.sleep(3) 
create_account_button.click()

print("okay")

time.sleep(3) 


try:
    # Check for the presence of the email field instead of visibility
    email_field = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
    send_keys_one_by_one(email_field, config["email"])

    next_button = wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
    next_button.click()

    # Continue with the rest of your script...
except TimeoutException:
    print("Email field or next button not found.")
    driver.quit()
