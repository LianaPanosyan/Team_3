from Pages.home_page import HomePage
from Pages.result_page import ResultPage
import logging
import config
import time


def test_case(driver):
    home_page = HomePage(driver)
    result_page = ResultPage(driver)
    try:
        logging.info("Starting test case!")
        home_page.open_url(config.url)
        home_page.search_object(config.search_data)
        time.sleep(3)
        result_page.select_brand_and_price()
        time.sleep(2)
        results = result_page.get_result()
        assert len(results) > 0, "No results found for that brand and price."

        for result in results:
            result_text = result.text.lower()
            assert "lacoste" in result_text, f"Result does not match brand: {result_text}"
            # Extract the price from the result text
            price_start = result_text.find("sale for $")
            if price_start != -1:
                price_start += len("sale for $")
                price_end = result_text.find(".", price_start)
                price_str = result_text[price_start:price_end].strip()
                price = float(price_str)
                assert price <= 200.00, f"Result price exceeds $200: {result_text}"
            else:
                raise AssertionError(f"Price not found in result: {result_text}")
            logging.info(f"Found result: {result.text}")
        logging.info(f"Found {len(results)} results.")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test completed")
