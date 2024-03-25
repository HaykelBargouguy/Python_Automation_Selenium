import json
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
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
    config_list = json.load(file)
for config in config_list:
   
    driver = webdriver.Chrome()
    driver.get(config["url"])


    email_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME,"identifier")))
    send_keys_one_by_one(email_field, config["email"])

    time.sleep(1)

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Next')]]")))
    next_button.click()

    time.sleep(0.5)

    next_button_2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Next')] and @jsname='LgbsSe']"))
    )
    next_button_2.click()



    email_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME,"identifier")))
    send_keys_one_by_one(email_field, config["email"])

    time.sleep(0.5)
    next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Next')]]"))
        )
    next_button.click()

    time.sleep(0.5)


    password_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "Passwd"))
    )

    send_keys_one_by_one(password_field, config["password"])

    next_button_after_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Next')]]"))


    )
    next_button_after_password.click()



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


    if submit_button:
        with open('GeneratedAccount.txt', 'w') as file:
            file.write('Email: ' + config["email"] + '\n')
            file.write('Password: ' + config["password"] + '\n')
    else:
        print("nothing is  new")

    driver.quit()






