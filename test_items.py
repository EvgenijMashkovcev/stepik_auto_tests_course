import time
from selenium.webdriver.common.by import By


def test_button_add_to_basket_exist_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_on_page = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button_on_page, "The specified button was not found"

