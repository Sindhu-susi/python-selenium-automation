from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given ('Open target product A-94109180 page')
def open_target_product_page(context):
    context.driver.get(f'https://www.target.com/p/women-s-flutter-short-sleeve-maxi-a-line-dress-a-new-day/-/A-94109180?preselect=93712592#lnk=sametab')
    sleep(10)

@then('Verify user can click through colours')
def verify_user_can_click_colours(context):
    expected_colours=['Black','Light Pink','Tan']
    actual_colours=[]

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)


    for c in colors:
     c.click()
     sleep(.5)
     selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
     print('Current color', selected_color)
     selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
     actual_colours.append(selected_color)
     print(actual_colours)

    assert expected_colours== actual_colours,f'Expected {expected_colours} colours, but found {actual_colours}'


