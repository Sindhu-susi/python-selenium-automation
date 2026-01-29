from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")

    def verify_search_results(self,search_product):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert search_product in actual_text, f'Expected text "{search_product}" not in actual text {actual_text}'