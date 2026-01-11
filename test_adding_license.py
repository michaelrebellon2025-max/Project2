from selenium import webdriver
import selenium
import time
from Urban_Routes_Main_page import UrbanRoutesMainPage
from run_urban_routes_main_page import urban_routes_page

def test_adding_license():
    driver = webdriver.Chrome()
    driver.get('https://cnt-85c07ff4-4e00-4318-bad1-260108799a0f.containerhub.tripleten-services.com')
    urban_routes_page= UrbanRoutesMainPage(driver)
#
    urban_routes_page.enter_from_location("East")
    urban_routes_page.enter_to_location("1300")
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_custom_car_icon()
    time.sleep(2)
    urban_routes_page.click_book()
    time.sleep(2)
    urban_routes_page.click_camping()
    time.sleep(2)
    urban_routes_page.click_drivers_license_icon()
    urban_routes_page.enter_first_name("Michael")
    urban_routes_page.enter_last_name("Feds")
    urban_routes_page.enter_birth_date("06.02.1994")
    urban_routes_page.enter_card_number("1234567891")
    time.sleep(2)
    urban_routes_page.click_add_card()
    time.sleep(2)
    actual_value= urban_routes_page.get_add_card_text()
    expected_value= "Thank you!"
    assert expected_value in actual_value, f'Expected "{expected_value}" but got "{actual_value}"'
    driver.quit()

