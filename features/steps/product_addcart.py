from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('User opens Target home page')
def step_open_target_home(context):
    context.driver.get("https://www.target.com")

    wait = WebDriverWait(context.driver, 20)

    # Wait for page to load
    wait.until(
        EC.presence_of_element_located(
            (By.ID, "search")
        )
    )

@when('User search for a product')
def step_add_product_to_cart(context):
        wait = WebDriverWait(context.driver, 20)

        # Search for a common product
        search_box = context.driver.find_element(By.ID, "search")
        search_box.send_keys("toothpaste")
        search_box.submit()
        sleep(10)

@when('User adds a product to the cart')
def click_add_to_cart(context):
    wait = WebDriverWait(context.driver, 25)
    cart_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[id*='addToCartButton']"))
    )

    # Click the first visible and enabled button
    for btn in cart_buttons:
        if btn.is_displayed() and btn.is_enabled():
            btn.click()
            break

    # Wait for side cart / content wrapper to appear
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")),
        message='Side navigation Add To Cart Btn not clickable'
    )

@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    wait = WebDriverWait(context.driver, 15)
    side_cart_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']"))
    )
    side_cart_button.click()

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')
    sleep(10)

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    wait = WebDriverWait(context.driver, 25)

    # Wait until subtotal / cart summary span appears
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")),
        message='Subtotal text did not appear'
    )

    # Get text
    cart_summary = context.driver.find_element(By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']").text

    # Assert expected amount
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
