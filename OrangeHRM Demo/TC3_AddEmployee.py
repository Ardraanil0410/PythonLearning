from dbm import error
from xml.etree.ElementTree import XMLParser

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.alert import Alert


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Login to application
username=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"username")))
username.send_keys("Admin")
password=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"password")))
password.send_keys("admin123")
login_button=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
login_button.click()

#To add a employee
#Step 1 : To navigate to Admin tab
admin_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
admin_tab.click()
print("Navigated to admin tab")

## To confirm we are on Admin tab
admin_heading=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='oxd-topbar-header']"))).text
# print(admin_heading)
## Clicking on Add button in the Admin page
add_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Add']")))
add_button.click()
## To confirm we are on the Add user page
form_title=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']"))).text

#Step 2: Entering user details
user_role_dropdown=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'oxd-select-text-input')][normalize-space()='-- Select --']")))
user_role_dropdown.click()
# user_role_dropdown.send_keys("Admin")
user_role_selection=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'oxd-select-option')][normalize-space()='Admin']")))
user_role_selection.click()
print("Admin role selected")
## Selecting employee name
Employee_Name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Type for hints...']")))
Employee_Name.send_keys("Christopher")
time.sleep(3)
listbox_html = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']"))).get_attribute("outerHTML")
print(listbox_html)
time.sleep(2)
employee_option=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@role='option']//span[text()='Christopher  Mcmillan']")))
time.sleep(2)
employee_option.click()
print("Employee name entered")

##Selecting Status
status_dropdown=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div")))
status_dropdown.click()
# print(status_dropdown.text)
enabled_option=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'oxd-select-option')][normalize-space()='Enabled']")))
enabled_option.click()
time.sleep(2)

##Entering username
username_text=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")))
username_text.clear()
username_text.send_keys("Lasttry")
print("Username has been entered")

##Entering password
password_text=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")))
password_text.clear()
password_text.send_keys("Selenium123")
print("Password has been entered ")

##Confirming password
confirm_pwd=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")))
confirm_pwd.send_keys("Selenium123")
print("Confirmed password")

##click on save
save_button=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]")
save_button.click()

## Message validation is pending

# //div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast oxd-toast-list-leave-active oxd-toast-list-leave-to']
# //div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast oxd-toast-list-leave-active oxd-toast-list-leave-to']
driver.quit()