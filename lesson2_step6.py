from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    input2 = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click()

    input3 = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:

    time.sleep(10)

    browser.quit()




