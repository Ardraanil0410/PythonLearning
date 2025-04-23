from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Invalid login attempt
username =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"username")))
username.send_keys("Ardra")
password=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"password")))
password.send_keys("Invalid")
login_button=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
login_button.click()

#error message validation
error_message =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))).text
print("Error message : ",error_message)
assert "Invalid credentials" in error_message

#close the browswer
driver.quit()