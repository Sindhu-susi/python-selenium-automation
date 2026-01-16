from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#Classwork and Homework 3
@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@then('Search results for tea are shown')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'

# HW3  Create a test case using BDD that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown

@when('Clicks on cart')
def click_cart(context):
    cart_icon = context.driver.find_element(By.XPATH, "//div[@class='sc-3d85a90e-1 fkOzcq']//*[name()='svg']")
    cart_icon.click()
    sleep(5)

@then('Verify "cart is empty" message shown')
def verify_cart_message(context):
    empty_cart=context.driver.find_element(By.XPATH, "//h1[contains(text(),'Your cart is empty')]")
    assert empty_cart.is_displayed(), "Empty cart message is not displayed"
    print("Test Passed: 'Your cart is empty' message is displayed")

#HW3 Create a test case using BDD to verify that a logged out user can navigate to Sign In

@when('User clicks sign in')
def sign_in(context):
    signin_account_button = context.driver.find_element(By.XPATH, "//a[@id='account-sign-in']")
    signin_account_button.click()
    sleep(4)
@when('User clicks sign in from right navigation menu')
def sign_in_menu(context):
 signin_btn=context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
 signin_btn.click()
 sleep(5)

@then('Verify sign in page opened')
def verify_sign_in_message(context):
    signin_txt=context.driver.find_element(By.XPATH,"//h1[contains(text(),'Sign in')]")
    signin_txt.click()
    assert signin_txt.is_displayed(), "Sign in page not opened"
    print("Test Passed: 'Sign in page opened and message is displayed")