from pages.base_page import BasePage
from playwright.sync_api import Page


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.sort_filter = page.get_by_test_id('filter-sort')
        self.apply_button = page.get_by_test_id('apply-filters-button')

    def get_all_prices(self, count):
        prices = []
        for i in range(1, count + 1):
            price = self.page.get_by_test_id(f'search-result-price-{i}').inner_text()
            price_ = int(price.replace(' RUB', ''))
            prices.append(price_)
        return prices

    def pick_filter(self, filter_type):
        self.sort_filter.select_option(filter_type)
        self.apply_button.click()
