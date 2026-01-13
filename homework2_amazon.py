from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(10)

driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']").click()
sleep(5)
#locator for amazon logo
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

#locator for email field
driver.find_element(By.ID,'ap_email_login')

#locator for continue button
driver.find_element(By.XPATH,"//input[@class='a-button-input']")

#locator for conditions
driver.find_element(By.XPATH,"//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

#locator for privacy notice
driver.find_element(By.XPATH,"//a[contains(@href, 'ap_signin_notification_privacy_notice')]")

#locator for Need help
driver.find_element(By.XPATH,"//a[normalize-space(text())='Need help?']")

#locator for create a free business account
driver.find_element(By.XPATH,"//span[normalize-space()='Create a free business account']")



