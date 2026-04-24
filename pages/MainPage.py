

from pages.BasePage import BasePage
from playwright.sync_api import Page




class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def search(self, query: str):
        self.search_input.click()
        self.search_button.fill(query)
        self.search_button.click()
