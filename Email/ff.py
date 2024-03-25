from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.uefa.com/euro2024/")

wait = WebDriverWait(driver, 20)
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'js-open-login')))
login_button.click()

# Attendre et fermer la boîte de dialogue des cookies, si présente
try:
    reject_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    reject_cookies_button.click()
except Exception as e:
    print("Pas de boîte de dialogue des cookies à fermer.")

# Attendre et cliquer sur "Create your UEFA account"
create_account_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create your UEFA account")))
create_account_button.click()

print("okay")

email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-75074230944436030'))
)
email_field.send_keys('your-email@example.com')

print("okay")

password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-password-59919533498235100'))
)
password_field.send_keys('bhbkgh1122*G')


first_name_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-130722358975432270'))
)
first_name_field.send_keys('HAYKEL')
# Pour le champ du nom de famille
last_name_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-30497114450394400'))
)
last_name_field.send_keys('bargouguiiiiii')

birth_day_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-88315185881230510'))
)
birth_day_input.send_keys('17')  


birth_month_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-105406014904922500'))
)
birth_month_input.send_keys('04') 

birth_year_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'gigya-textbox-32538633360993784'))
)
birth_year_input.send_keys('2000')

terms_checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'gigya-checkbox-terms'))
)
driver.execute_script("arguments[0].click();", terms_checkbox)

newsletter_checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'gigya-checkbox-75848120112080240'))
)
driver.execute_script("arguments[0].click();", newsletter_checkbox)


submit_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gigya-input-submit[type="submit"][value="Create account"]'))
)
submit_button.click()


print("okay")
 