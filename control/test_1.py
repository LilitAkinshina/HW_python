import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()

def test_form(setup):
    driver = setup

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")


    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    WebDriverWait(driver, 40, 0.1).until(EC.staleness_of(submit_button))

    assert "danger" in driver.find_element(By.ID, 'zip-code').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'first-name').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'last-name').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'address').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'e-mail').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'phone').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'city').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'country').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'job-position').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'company').get_attribute("class")
