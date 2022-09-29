from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    input1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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



