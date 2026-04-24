from pages.BasePage import BasePage
from playwright.sync_api import Page


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.sort_filter = page.get_by_test_id('filter-sort')

    def get_all_prices(self, count):
        prices = []
        for i in range(1,count):
            price = self.page.get_by_test_id(f'search-result-prices-{i}')
            price.inner_text()
            prices.append(price)
        return prices

    def pick_filter(self, filter_type):
        self.sort_filter.select_option(filter_type)