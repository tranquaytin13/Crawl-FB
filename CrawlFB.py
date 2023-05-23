import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

email = driver.find_element(by = 'id',value="email")
password = driver.find_element(by = 'id',value="pass")
email.send_keys("lewixa4254@marikuza.com")
password.send_keys("0985478445")
login_button = driver.find_element_by_name("login")
login_button.click()