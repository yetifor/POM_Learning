from pages.main_page import MainPage
from pages.search_page import SearchPage
from utils.enums import Sorting
import pytest
from utils.config_reader import ConfigReader

config = ConfigReader()


@pytest.mark.parametrize('states_count, type_filter', [(10, Sorting.LOW_TO_HIGH), (15, Sorting.HIGH_TO_LOW)])
@pytest.mark.parametrize('category', ['city', 'habits'])
def test_sorted1(page, category, states_count, type_filter):
    main_page = MainPage(page)
    search_page = SearchPage(page)
    main_page.page.goto(config.get('url'))
    main_page.search(category)
    search_page.pick_filter(type_filter)
    if type_filter == Sorting.LOW_TO_HIGH:
        search_page.page.wait_for_url('**sort=price_asc**')
        res = search_page.get_all_prices(states_count)
        print(res)
        assert res == sorted(res), (f'Получен резуьтат: actual = {res} '
                                    f'Фильтр сорировки:{type_filter}'
                                    f'Кол-во объектов: {states_count}'
                                    f'Ожидался результат: expected result = {sorted(res)}')

    elif type_filter == Sorting.HIGH_TO_LOW:
        search_page.page.wait_for_url('**sort=price_desc**')
        res = search_page.get_all_prices(states_count)
        print(res)
        assert res == sorted(res, reverse=True), (f'Получен резуьтат: actual = {res}'
                                                  f'Фильтр сорировки:{type_filter}'
                                                  f'Кол-во объектов: {states_count}'
                                                  f'Ожидался результат: expected result = {sorted(res, reverse=True)}')
