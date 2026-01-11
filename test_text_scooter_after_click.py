import time

import selenium
from selenium import webdriver

from Urban_Routes_Main_page import UrbanRoutesMainPage
from run_urban_routes_main_page import SERVER_URL
SERVER_URL1= "https://cnt-32cb5066-bdbb-4f0d-a127-bfa08cdac2a3.containerhub.tripleten-services.com"
driver = selenium.webdriver.Chrome()
driver = webdriver.Chrome()
driver.get(SERVER_URL1)
time.sleep(2)
urban_routes_page = UrbanRoutesMainPage(driver)

def test_scooter_button_click():
    urban_routes_page.enter_from_location("East")
    urban_routes_page.enter_to_location("1300")
    time.sleep(2)
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_scooter_icon()
    time.sleep(2)
    actual_value=urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value,f'Expected {expected_value} but got {actual_value}'
    driver.quit()
