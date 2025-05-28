from AutomationProject import data, helpers
import time
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Check if the URL is still running
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.enter_from_location(data.ADDRESS_FROM)
        pages.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)

        actual_value = pages.get_taxi_text()
        expected_value = "Taxi"
        assert expected_value in actual_value, f"Expected '{expected_value}' but got '{actual_value}'"

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.click_supportive_plan()

        actual_value = pages.get_active_plan()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}' but got '{actual_value}'"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.fill_in_phone_number(data.PHONE_NUMBER)

        assert pages.get_actual_phone() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.fill_in_card()

        actual_value = pages.get_actual_payment_method()
        expected_value = "Card"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"


    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.enter_comment(data.MESSAGE_FOR_DRIVER)

        actual_value = pages.get_actual_comment()
        assert actual_value == data.MESSAGE_FOR_DRIVER, f"Expected '{data.MESSAGE_FOR_DRIVER}', but got '{actual_value}'"

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.click_supportive_plan()
        pages.click_blanket_and_handkerchiefs()

        assert pages.get_blanket_and_handkerchiefs_status()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.click_supportive_plan()
        pages.order_ice_creams()

        actual_value = pages.get_ice_cream_counter_value()
        expected_value = "2"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        pages = UrbanRoutesPage(self.driver)

        pages.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        pages.click_supportive_plan()
        pages.enter_comment(data.MESSAGE_FOR_DRIVER)
        pages.click_order_taxi()

        assert pages.car_search_model_appears()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()