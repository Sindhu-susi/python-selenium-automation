from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
# open the url
driver.get('https://stackoverflow.com/users/signup')
sleep(10)

#locator for Create your account
driver.find_elements(By.CSS_SELECTOR, 'h1.flex--item.fs-headline1.fw-bold.lh-xs.mb8.ws-nowrap')

#locatorfor By clicking "Sign up"
driver.find_element(By.CSS_SELECTOR,'div.js-terms')

#locator for Email and Password
driver.find_element(By.CSS_SELECTOR,'input#email.s-input')
driver.find_element(By.CSS_SELECTOR,'input#password.flex--item.s-input')

#locator for show password
driver.find_element(By.CSS_SELECTOR,'svg.js-show-password')

#locator for sign up
driver.find_element(By.CSS_SELECTOR,'button#submit-button.flex--item.s-btn.s-btn__filled')

#locator for sign up with google
driver.find_element(By.CSS_SELECTOR,'button.s-btn__google')

#locator for sign up with GitHub
driver.find_element(By.CSS_SELECTOR,'button.s-btn__github')

#locator for get stackoverflow for terams free for upto 50 users
driver.find_element(By.CSS_SELECTOR, "a[href*='stackoverflow.com/teams']")





