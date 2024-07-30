from Calcmainpage import CalcMain
from selenium import webdriver
import pytest


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit


def test_calculator_assert(chrome_browser):
    calmain = CalcMain(chrome_browser)
    calmain.insert_time()
    calmain.clicking_buttons()


    assert "15" in calmain.wait_button_gettext()
