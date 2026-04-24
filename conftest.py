import pytest
from pages.BasePage import BasePage
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from utils.ConfigReader import ConfigReader

@pytest.fixture
def main(page)->MainPage:
    return MainPage(page)

@pytest.fixture
def search(page)->SearchPage:
    return SearchPage(page)

config = ConfigReader()

@pytest.fixture
def pull_url(page)->str:
    return config.get('url')