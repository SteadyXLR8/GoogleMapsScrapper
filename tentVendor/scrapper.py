import time
from typing import List, Dict

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import tentVendor.constants as const

# imports for explicit wait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# imports for stopping browser window close
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# Generic type for Data
T = Dict[str, str]


def scrollTo(element, scroll_count):
    for i in range(scroll_count):
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(const.SCROLL_TIMEOUT)

    return True


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        super(Booking, self).__init__()
        self.teardown = teardown
        self.teardown = self.teardown
        self.implicitly_wait(const.IMPLICIT_WAIT_TIME)
        self.maximize_window()
        self.data_array: List[T] = []
        # self.options = chrome_options

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.close()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def enter_search_text(self, text):
        # clicking search button
        search_box = self.find_element(By.ID, const.SEARCH_BOX_ID)
        search_box.clear()
        search_box.send_keys(text)
        search_box.send_keys(Keys.ENTER)
        time.sleep(const.SEARCH_TIMEOUT)  # Wait for results to load

    def collect_data(self):
        try:
            # getting the feed container
            feed_container = self.find_elements(By.CSS_SELECTOR, const.RESULT_FEED_SELECTOR)
            # scroll all the possible results returned from the search -> loads all the data

            if scrollTo(feed_container[0], const.SCROLL_FEED_COUNTER):

                # getting the updated list and each item
                container = self.find_element(By.CSS_SELECTOR, const.RESULT_FEED_SELECTOR)
                results = container.find_elements(By.CLASS_NAME, const.RESULT_ITEM_CLASS)

                for item in results:
                    # getting the link -> extracts very large link-> requires shortener
                    linkItem = item.find_element(By.CLASS_NAME, const.RESULT_LINK_CLASS)
                    # link = linkItem.get_attribute(const.HREF_ATTRIBUTE)
                    # getting business name
                    name = item.find_element(By.CLASS_NAME, const.RESULT_NAME_CLASS).text
                    # to avoid overlapping item with "Back to top" button -> bring item in focus
                    self.execute_script(const.BRING_IN_FOCUS_SCRIPT, item)
                    time.sleep(const.TIMEOUT_AFTER_SCRIPT_EXE)
                    linkItem.click()
                    time.sleep(const.TIMEOUT_AFTER_CLICK)
                    # find address
                    try:
                        address_container = self.find_element(By.CSS_SELECTOR, const.RESULT_ADDRESS_SELECTOR)
                        address = address_container.text
                    except NoSuchElementException:
                        address = const.NOT_AVAILABLE
                    # find phone number
                    try:
                        phone_container = self.find_element(By.CSS_SELECTOR, const.RESULT_PHONE_SELECTOR)
                        phone = phone_container.text
                    except NoSuchElementException:
                        phone = const.NOT_AVAILABLE

                    # find the shorter link
                    try:
                        share_button = self.find_element(By.CSS_SELECTOR, const.SHARE_BUTTON_SELECTOR)
                        share_button.click()

                        # input element to extract the shorter link
                        link_input = self.find_element(By.CLASS_NAME, const.LINK_INPUT_SELECTOR)
                        link = link_input.get_attribute("value")

                        # close the modal
                        close_modal_button = self.find_element(By.CSS_SELECTOR, const.CLOSE_BUTTON_SELECTOR)
                        close_modal_button.click()
                    except NoSuchElementException:
                        link = const.NOT_AVAILABLE
                    # creating data object
                    data:T = {
                        "Name": name,
                        "Address": address,
                        "Phone": phone,
                        "Link": link
                    }
                    # storing data object to array
                    self.data_array.append(data)
                    # clicking the close button
                    button = self.find_element(By.CSS_SELECTOR, const.CLOSE_ITEM_INFO_WINDOW_SELECTOR)
                    button.click()
        except Exception as e:
            print(f"{const.ERROR_MESSAGE}{e}")

    def getData(self):
        return self.data_array
