import json
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_keys_one_by_one(element, text, delay=0.05):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)


with open('config.json', 'r') as file:
    config_list = json.load(file)


for config in config_list:
    
          driver = webdriver.Chrome()
          driver.get("https://copaamerica.com/en/?fbclid=IwAR2itmSA6ao_3_6WP2UoAHBkJKSMINEiADNBpbISbZxq5w9x5_1TRaNiMrE")


          iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.lazyloaded")))
          driver.switch_to.frame(iframe)

          first_name_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "FirstName")))
          
          first_name_field.send_keys(config["FirstName"])



          last_name_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"LastName")))
          time.sleep(0.5) 
          send_keys_one_by_one(last_name_field, config["LastName"])


          email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,"Email")))
          time.sleep(0.5) 
          send_keys_one_by_one(email_field, config["Email"])


          zipcode_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,"ZipCode")))
          time.sleep(0.5) 
          send_keys_one_by_one(zipcode_field, config["ZipCode"])

          team_select_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "favoriteNationalteam")))
          
          team_select = Select(team_select_element)
          team_select.select_by_value("Brazil")


          optin_checkbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "optin")))
          if not optin_checkbox.is_selected():
                    optin_checkbox.click()


          submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
          )
          time.sleep(0.5)
          submit_button.click()

          data_to_save = {
          "FirstName": config["FirstName"],
          "LastName": config["LastName"],
          "Email": config["Email"],
          "ZipCode": config["ZipCode"],
          }

          with open('NewInscription.txt', 'a') as file:
                    for key, value in data_to_save.items():
                               file.write(f"{key}: {value}\n")