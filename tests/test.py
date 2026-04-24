import pytest
import conftest
from utils.enums import Sorting
from utils.ConfigReader import ConfigReader
from pages.BasePage import BasePage
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
config = ConfigReader()

@pytest.mark.parametrize('category, states_count, type_filter', [
    ('city', 10, Sorting.LOW_TO_HIGH),
    ('city', 15, Sorting.HIGH_TO_LOW),
    ('habits', 10, Sorting.LOW_TO_HIGH),
    ('habits', 15, Sorting.HIGH_TO_LOW)
])
def test_sorted(page, main,search, category, states_count, type_filter):
    page.goto(config.get('url'))
    main.search(category)
    search.pick_filter(type_filter)
    print(search.get_all_prices(states_count))
    assert 15-1 == 12

def test_example():
    assert 1 + 1 == 2

def test_another_example():
    assert True


