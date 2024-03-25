import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_data_dir = tempfile.mkdtemp()

chrome_options = Options()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--allow-running-insecure-content")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://stackoverflow.com/users/login"
driver.get(url)

wait = WebDriverWait(driver, 10)

google_login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-btn__google")))
google_login_button.click()

email_field = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
email_field.send_keys("sadokgaied@gmail.com")

next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "identifierNext"))
)
next_button.click()

time.sleep(5)

driver.quit()
