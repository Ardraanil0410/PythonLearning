from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(driver,10)

#Login flow
username = driver.find_element(By.NAME,"username")
username.send_keys("Admin")
password =driver.find_element(By.NAME,"password")
password.send_keys("admin123")

login_button=driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
print("Login successful") # message displayed once the login is successful

#Logout flow
menu=driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
menu.click()

logout=driver.find_element(By.LINK_TEXT,"Logout")
logout.click()
print("Logout successful") # message displayed once the logout is successful

# closes all the browsers
driver.quit()
