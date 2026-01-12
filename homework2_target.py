from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
sleep(5)

account_button= driver.find_element(By.XPATH,"//a[@id='account-sign-in']")
account_button.click()
sleep(5)

signin_button= driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']")
driver.execute_script("arguments[0].scrollIntoView(true);", signin_button)

signin_button.click()
sleep(10)


signin_text= driver.find_element(By.XPATH,"//h1[contains(text(),'Sign in or create account')]")

print(f"The sign in text found",signin_text.text)

login_button=driver.find_element(By.XPATH,"//button[@type='submit' and @id='login']")
sleep(5)
if login_button:
    print("Sign in button is present and test case passed")
else:
    print("Sign in button is not present and  test case failed")

driver.quit()
