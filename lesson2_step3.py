from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"
try:

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")

    y = browser.find_element(By.ID, "num2")

    s = int(x.text) + int(y.text)

    s1 = str(s)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(s1)

    time.sleep(1)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:

    time.sleep(6)
    browser.quit()

