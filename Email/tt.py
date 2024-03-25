import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Charger les données depuis config.json
with open('config.json', 'r') as file:
    config = json.load(file)    


chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--use_subprocess")

driver = uc.Chrome(options=chrome_options)

driver.get(config["url"])

wait = WebDriverWait(driver, 20)
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'js-open-login')))
login_button.click()

try:
    reject_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    reject_cookies_button.click()
except Exception as e:
    print("Pas de boîte de dialogue des cookies à fermer.")

create_account_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create your UEFA account")))
create_account_button.click()

print("okay")

email_field = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-75074230944436030'))
)
email_field.send_keys(config["email"])

password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-password-59919533498235100'))
)
password_field.send_keys(config["password"])

first_name_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-130722358975432270'))
)
first_name_field.send_keys(config["first_name"])

last_name_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-30497114450394400'))
)
last_name_field.send_keys(config["last_name"])



driver.execute_script("document.getElementById('gigya-textbox-88315185881230510').value = arguments[0];", config["DD"])
driver.execute_script("document.getElementById('gigya-textbox-105406014904922500').value = arguments[0];", config["MM"])
driver.execute_script("document.getElementById('gigya-textbox-32538633360993784').value = arguments[0];", config["YYYY"])





terms_checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'gigya-checkbox-terms'))
)
driver.execute_script("arguments[0].click();", terms_checkbox)

newsletter_checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'gigya-checkbox-75848120112080240'))
)
driver.execute_script("arguments[0].click();", newsletter_checkbox)
 

submit_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gigya-input-submit[type="submit"][value="Create account"]'))
)
submit_button.click()


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