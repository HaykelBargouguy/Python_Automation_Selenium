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

create_account_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create your UEFA account")))
time.sleep(3) 
create_account_button.click()

print("okay")

email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-75074230944436030'))
)
time.sleep(3) 
send_keys_one_by_one(email_field, config["email"])

password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-password-59919533498235100'))
)
time.sleep(3)
send_keys_one_by_one(password_field, config["password"])

first_name_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-130722358975432270'))
)
time.sleep(3) 
send_keys_one_by_one(first_name_field, config["first_name"])

last_name_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-30497114450394400'))
)
time.sleep(3) 
send_keys_one_by_one(last_name_field, config["last_name"])


birth_day_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-88315185881230510'))
)
time.sleep(3) 
send_keys_one_by_one(birth_day_input, config["DD"])


birth_month_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-105406014904922500'))
)
time.sleep(3) 
send_keys_one_by_one(birth_month_input, config["MM"])

birth_year_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-32538633360993784'))
)
time.sleep(3) 

send_keys_one_by_one(birth_year_input, config["YYYY"])

terms_checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'gigya-checkbox-terms'))
)
time.sleep(3) 

driver.execute_script("arguments[0].click();", terms_checkbox)

newsletter_checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'gigya-checkbox-75848120112080240'))
)
time.sleep(3) 

driver.execute_script("arguments[0].click();", newsletter_checkbox)
 

submit_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gigya-input-submit[type="submit"][value="Create account"]'))
)
time.sleep(3) 
submit_button.click()


api_key = '2fbd950e0ce8f5ed1c3957d80d741ec7'
sitekey = "6LehfZUbAAAAAJhue_6BVqqxLulLiXLP0rEgpdRH"

client = AnticaptchaClient(api_key)


task = NoCaptchaTaskProxylessTask(config["url"], sitekey)


solver = recaptchaV2Proxyless()
solver.set_verbose(1)  
solver.set_key(api_key)
solver.set_website_url(config["url"])
solver.set_website_key(sitekey)

# Récupérez la solution du CAPTCHA
g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g_response: " + g_response)
else:
    print("Task finished with error: " + solver.error_code)



print("okay")

if submit_button:
    with open('data.txt', 'w') as file:
        file.write('Email: ' + config["email"] + '\n')
        file.write('Password: ' + config["password"] + '\n')
    print("We have a new inscription data.txt")
else:
    print("nothing is  new")

input("Appuyez sur Enter pour fermer le navigateur...")
driver.quit()