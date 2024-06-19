from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging
import time


class ResultPage(BasicHelper):
    result = (By.XPATH, "//a[@class='Bn-z']")

    def select_brand_and_price(self, brand_name, price):
        brand_name_filter = (By.XPATH, f"//ul[@aria-labelledby='brandNameFacet']//span[text()='{brand_name}']")
        brand_price_filter = (By.XPATH, f"//a[@class='uA-z']//span[text()='${price} and Under']")
        try:
            time.sleep(2)
            # Find and scroll to the brand element
            brand_name_element = self.find_elem_ui(brand_name_filter)
            self.scroll_to_element(brand_name_element)
            self.find_and_click(brand_name_filter)

            logging.info(f"Selected brand: {brand_name_element.text}")

            time.sleep(3)

            # Find and click the price element
            brand_price_element = self.find_elem_ui(brand_price_filter)
            self.find_and_click(brand_price_filter)

            logging.info(f"Selected price: {brand_price_element.text}")

            time.sleep(2)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def get_result(self):
        time.sleep(1)
        search_results = self.find_elements(self.result)
        time.sleep(2)
        return search_results
