from selenium import webdriver
import selenium
import time
from Urban_Routes_Main_page import UrbanRoutesMainPage
from run_urban_routes_main_page import urban_routes_page


def test_car_brand():
    driver = webdriver.Chrome()
    driver.get("https://cnt-5f4b1df5-0297-45b3-9669-a28747baabd1.containerhub.tripleten-services.com")
    time.sleep(2)
    urban_routes_page = UrbanRoutesMainPage(driver)

    urban_routes_page.enter_from_location("East")
    urban_routes_page.enter_to_location("1300")
    time.sleep(2)
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_custom_car_icon()
    time.sleep(2)
    urban_routes_page.click_book()
    time.sleep(2)
    urban_routes_page.click_camping()
    time.sleep(2)
    actual_value=urban_routes_page.get_camping_text()
    expected_value="Audi A3 Sedan"
    assert expected_value in actual_value, f'Expected {expected_value}, but got {actual_value}'
    driver.quit()