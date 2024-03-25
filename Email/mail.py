import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp20RKHoaOIlEChxI3TVegPXNa4KjVS190N0vCF8IsEDFninNTKiVsf7TGkmnC6K3m3-04Yyzg&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1576189271%3A1701618388400227&theme=glif"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
driver.get(url)

email_field = driver.find_element(By.ID, "identifierId")

email_field.send_keys("bargougui.haikel@gmail.com")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "identifierNext"))
    )
next_button.click()


password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Password")))

password_field.send_keys("Haykel2001*")




sign_in_button = driver.find_element(By.ID, "passwordNext")
sign_in_button.click()


time.sleep(100)

# Fermez le navigateur
