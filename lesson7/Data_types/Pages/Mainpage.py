from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson7.URL import form_url
from lesson7.Data_types.data import *

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(form_url)
        
    def find_fields(self):
        self.first_name = (By.NAME, "first-name")
            