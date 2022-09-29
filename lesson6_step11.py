from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//div[@class='form-group first_class']/input[@required]")
    input1.send_keys("Evgenii")
    input2 = browser.find_element(By.XPATH, "//div[@class='form-group second_class']/input[@required]")
    input2.send_keys("Mashkovtsev")
    input3 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']/input[@required]")
    input3.send_keys("Sss123sk@mail.ru")

    # Проверяем что поля заполнены
    time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    # сделал 2 секунды вместо одной потому что может не успеть пройти :)
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

