from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    #инициализируем браузер
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    #жмякаем кнопочку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    #переключаемся на alert и подтверждаем его
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #находим локатор "x" и вносим значение "x" в переменную "У"
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    #вносим полученное значени в поле для ответа
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    #отправляем данные
    button = browser.find_element(By.XPATH, "//button")
    button.click()


finally:
    # закрываем браузер после всех манипуляций с задержкой в 5 сек
    time.sleep(5)
    browser.quit()