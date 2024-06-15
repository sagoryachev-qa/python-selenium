from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    #считаем то что указанно в "x" на странице
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    #находим локатор "x" и вносим значение "x" в переменную "У"
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    #вносим полученное значени в поле для ответа
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    #выставляем чекбокс и радиобаттон
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()
    #отправляем данные
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

