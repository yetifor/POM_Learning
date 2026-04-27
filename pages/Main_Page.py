from pages.Base_Page import BasePage


class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def search(self, category: str):
        self.search_input.click()
        self.search_input.fill(category)
        self.search_button.click()
