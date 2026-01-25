from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# open the url
driver.get('https://www.target.com/')
sleep(5)

#account_button= driver.find_element(By.XPATH,"//a[@id='account-sign-in']")
account_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@id='account-sign-in']")))
account_button.click()
#sleep(5)

#signin_button= driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']")
signin_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-test='accountNav-signIn']")))
driver.execute_script("arguments[0].scrollIntoView(true);", signin_button)

signin_button.click()
#sleep(10)


#signin_text= driver.find_element(By.XPATH,"//h1[contains(text(),'Sign in or create account')]")
signin_text=wait.until(EC.element_to_be_clickable((By.XPATH,"//h1[contains(text(),'Sign in or create account')]")))
print(f"The actual text is",signin_text.text)

expected_text = "Sign in or create account"
assert signin_text.text ==expected_text, f"Expected '{expected_text}' but got '{signin_text.text}'"
print('Test case passed')

#login_button=driver.find_element(By.XPATH,"//button[@type='submit' and @id='login']")
#sleep(5)

login_button= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit' and @id='login']")))
if login_button:
    print("Sign in button is present and test case passed")
else:
    print("Sign in button is not present and  test case failed")

driver.quit()
