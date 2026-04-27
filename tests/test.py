from pages.Main_Page import MainPage
from pages.Search_Page import SearchPage
from utils.enums import Sorting

import pytest
from utils.Config_Reader import ConfigReader

config = ConfigReader()


@pytest.mark.parametrize('category, states_count, type_filter', [
    ('city', 10, Sorting.LOW_TO_HIGH),
    ('city', 15, Sorting.HIGH_TO_LOW),
    ('habits', 10, Sorting.LOW_TO_HIGH),
    ('habits', 15, Sorting.HIGH_TO_LOW)
])
def test_sorted1(page, category, states_count, type_filter):
    main_page = MainPage(page)
    search_page = SearchPage(page)
    main_page.page.goto(config.get('url'))
    main_page.search(category)
    search_page.pick_filter(type_filter)
    search_page.page.wait_for_timeout(5000)
    res = search_page.get_all_prices(states_count)
    print(res)
    if type_filter == Sorting.LOW_TO_HIGH:
        assert res == sorted(res), 'цены не отсортированы по возрастанию'
    elif type_filter == Sorting.HIGH_TO_LOW:
        assert res == sorted(res, reverse=True), 'цены не отсортированы по убыванию'

