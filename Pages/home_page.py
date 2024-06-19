from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging
import time
from selenium.webdriver.common.keys import Keys


class HomePage(BasicHelper):
    search_field = (By.ID, 'searchAll')

    def search_object(self, object_name):
        search_field = self.find_elem_ui(self.search_field)
        search_field.clear()
        search_field.send_keys(object_name)
        search_field.send_keys(Keys.ENTER)
        time.sleep(3)
        logging.info(f"Searched data: {object_name}")
