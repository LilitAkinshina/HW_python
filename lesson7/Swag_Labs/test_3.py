from Shopmain import ShopmainPage
from ShopContainer import ShopContainer
import pytest
from selenium import webdriver


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit


def test_shop(chrome_browser):
    expected_total = "58.29"

    shopmain = ShopmainPage(chrome_browser)
    shopmain.registration_fields()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.into_container()

    container = ShopContainer(chrome_browser)
    container.checkout()
    container.info()
    container.price()
    assert expected_total in container.price()
    print(f"Итого ${container.price()}")
