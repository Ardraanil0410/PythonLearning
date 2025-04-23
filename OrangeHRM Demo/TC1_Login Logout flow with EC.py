from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Login flow
username = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"username")))
username.send_keys("Admin")
password=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"password")))
password.send_keys("admin123")

login_button=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
login_button.click()
print("Login successful") # message displayed once the login is successful

#Logout flow
menu =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")))
menu.click()

logout=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,"Logout")))
logout.click()
print("Logout successful") # message displayed once the logout is successful

# closes all the browsers
driver.quit()



