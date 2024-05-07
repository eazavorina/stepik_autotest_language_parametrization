from selenium.webdriver.common.by import By
import time


def test_product_page_should_contain_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # Ниже ожидание для удобства ревью :)
    # time.sleep(15)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Add to basket button is not displayed"

