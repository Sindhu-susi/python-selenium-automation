from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('User opens Target Circle page')
def step_open_target_circle(context):
    context.driver.get("https://www.target.com/circle")
    sleep(10)

@then('unlock added value section shows 2 story cards')
def verify_circle_card(context):
    wait = WebDriverWait(context.driver, 20)
    #context.driver.find_element(By.XPATH,"//h2[normalize-space()='Unlock added value']")
    #sleep(5)
    #cards = context.driver.find_elements(By.XPATH,"//div[@data-test='@web/SlingshotComponents/common/Storycard']")
    cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//h2[contains(., 'Unlock added value')]/following::*[1]//a")))

    print(cards)

    assert len(cards) == 2, f"Expected 2 story cards, found {len(cards)}"

