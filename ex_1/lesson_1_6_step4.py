from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html" #ссылка на которую будет переходить браузер

try:
    #инициализируем браузер
    browser = webdriver.Chrome()
    browser.get(link)
    #заполняем форму
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input4 = browser.find_element(By.CLASS_NAME, "city")
    input4.send_keys("123")
    input5 = browser.find_element(By.ID, "country")
    input5.send_keys("Russia")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций с задержкой в 5 сек
    time.sleep(5)
    browser.quit()