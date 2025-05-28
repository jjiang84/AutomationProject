import time
from selenium.webdriver import Keys
from AutomationProject import data, helpers
from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    TAXI_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')
    TAXI_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    CALL_A_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    ACTIVE_PLAN_LOCATOR = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    SUPPORTIVE_LOCATOR = (By.XPATH, '//div[contains(text(),"Supportive")]')
    PHONE_NUMBER_FILL_LOCATOR = (By.CLASS_NAME, "np-text")
    PHONE_NUMBER_LOCATOR = (By.ID, 'phone')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    SMS_CODE_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"Confirm")]')
    PAYMENT_METHOD_LOCATOR = (By.CLASS_NAME, "pp-value-text")
    ADD_CARD_LOCATOR = (By.CLASS_NAME, "pp-plus")
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CODE_NUMBER_LOCATOR = (By.NAME, 'code')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"Link")]')
    CLOSE_PAYMENT_METHOD_LOCATOR = (By.CSS_SELECTOR, ".payment-picker.open .close-button")
    COMMENT_LOCATOR = (By.NAME, "comment")
    ORDER_REQUIREMENTS_LOCATOR = (By.CLASS_NAME, "reqs-head")
    BLANKET_AND_HANDKERCHIEFS_LOCATOR = (By.CLASS_NAME, "switch")
    BLANKET_AND_HANDKERCHIEFS_SELECTOR_LOCATOR = (By.CSS_SELECTOR, ".switch-input")
    ORDER_ICE_CREAM_COUNTER_LOCATOR = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAM_COUNTER_VALUE_LOCATOR = (By.XPATH, '//div[@class="counter-value"]')
    ORDER_TAXI_LOCATOR = (By.CLASS_NAME, "smart-button-main")
    CAR_SEARCH_LOCATOR = (By.XPATH,'//div[text()="Car search"]')

    def __init__(self, driver):
        self.driver = driver # Initialize the driver

    # Step to enter both "From" and "To" locations

    def enter_from_location(self, from_text):
        # Type the "From" location
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Type the "To" location
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    # Return the taxi text
    def get_taxi_text(self):
        return self.driver.find_element(*self.TAXI_TEXT_LOCATOR).text

    # Click call a taxi button
    def click_taxi_button(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON_LOCATOR).click()

    # Click supportive plan
    def click_supportive_plan(self):
        #self.driver.find_element(*self.SUPPORTIVE_LOCATOR).click()
        # Check if the supportive plan is selected or not to avoid unnecessary clicks
        if self.driver.find_element(*self.ACTIVE_PLAN_LOCATOR).get_attribute("textContent") != "Supportive":
            self.driver.find_element(*self.SUPPORTIVE_LOCATOR).click()
        else:
            print("Supportive plan is already selected, don't click")

    def get_active_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_LOCATOR).get_attribute("textContent")

    # Click phone number text
    def click_phone_number_text(self):
        self.driver.find_element(*self.PHONE_NUMBER_FILL_LOCATOR).click()

    #Return phone number text
    def get_actual_phone(self):
        return self.driver.find_element(*self.PHONE_NUMBER_FILL_LOCATOR).text

    # Enter phone number
    def enter_phone_number(self,phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(phone_number)

    # Click next button
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    # Enter SMS code
    def enter_sms_code(self,code):
        self.driver.find_element(*self.SMS_CODE_LOCATOR).send_keys(code)

    # Click confirm button
    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    # Click payment method
    def click_payment(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    # Click add card
    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    # Enter card number
    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

    # Enter code
    def enter_code(self, code_number):
        self.driver.find_element(*self.CODE_NUMBER_LOCATOR).send_keys(code_number)

    # Click link button
    def click_link_button(self):
        self.driver.find_element(*self.CODE_NUMBER_LOCATOR).send_keys(Keys.TAB)
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    # Click close payment method pop-up
    def click_close_payment_method(self):
        self.driver.find_element(*self.CLOSE_PAYMENT_METHOD_LOCATOR).click()

    def get_actual_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).get_property('textContent')

    # Enter comment
    def enter_comment(self, comment):
        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(comment)

    def get_actual_comment(self):
        return self.driver.find_element(*self.COMMENT_LOCATOR).get_attribute("value")

    # Click blanket and handkerchiefs
    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_LOCATOR).click()

    def get_blanket_and_handkerchiefs_status(self):
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_SELECTOR_LOCATOR).get_property("checked")

    # Order ice cream
    def click_ice_cream_counter(self):
        self.driver.find_element(*self.ORDER_ICE_CREAM_COUNTER_LOCATOR).click()

    def get_ice_cream_counter_value(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER_VALUE_LOCATOR).text

    # Order taxi
    def click_order_taxi(self):
        self.driver.find_element(*self.ORDER_TAXI_LOCATOR).click()

    # Step to enter From, To, and to click custom option, taxi icon, taxi text
    def set_route(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        time.sleep(2)
        self.click_taxi_button()

    # Step to fill in phone number
    def fill_in_phone_number(self, phone_number):
        self.click_phone_number_text()
        time.sleep(2)
        self.enter_phone_number(phone_number)
        time.sleep(2)
        self.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        time.sleep(1)
        self.enter_sms_code(code)
        time.sleep(2)
        self.click_confirm_button()
        time.sleep(2)

    # Step to fill in card
    def fill_in_card(self):
        self.click_payment()
        time.sleep(2)
        self.click_add_card()
        time.sleep(2)
        self.enter_card_number(data.CARD_NUMBER)
        time.sleep(2)
        self.enter_code(data.CARD_CODE)
        time.sleep(2)
        self.click_link_button()
        time.sleep(2)
        self.click_close_payment_method()
        time.sleep(2)

    # Step to order ice cream
    def order_ice_creams(self):
        num_ice_creams = 2
        # Adding loop to iterate twice for order_2_ice_cream
        for ice_cream in range(num_ice_creams):
            self.click_ice_cream_counter()
            time.sleep(2)

    # Step for car search model appears
    def car_search_model_appears(self):
        return self.driver.find_element(*self.CAR_SEARCH_LOCATOR).is_displayed()








