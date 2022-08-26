from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\User\Desktop\Temp3\chromedriver\chromedriver.exe')
driver.get("https://www.linkedin.com/")
time.sleep(4)


logging = driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary")
time.sleep(3)
logging.click()
time.sleep(3)

login = driver.find_element_by_id("username")
login.send_keys("********")
password = driver.find_element_by_id("password")
password.send_keys("*******")
enter = driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large")
enter.click()
time.sleep(2)


driver.quit()

