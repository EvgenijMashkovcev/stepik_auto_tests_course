from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"


try:

    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button1 = browser.find_element(By.XPATH, "// button[ @ id = 'book']")
    button1.click()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input2.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:

    time.sleep(10)

    browser.quit()
