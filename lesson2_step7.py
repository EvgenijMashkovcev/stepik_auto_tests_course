from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@name='firstname']")
    input1.send_keys("Evgenii")

    input2 = browser.find_element(By.XPATH, "//input[@name='lastname']")
    input2.send_keys("Mashkovtsev")

    input3 = browser.find_element(By.XPATH, "//input[@name='email']")
    input3.send_keys("EvgMash@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example1.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:

    time.sleep(10)

    browser.quit()



