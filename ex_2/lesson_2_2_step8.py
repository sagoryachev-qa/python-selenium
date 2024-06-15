from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    #инициализируем браузер
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")
    #заполняем форму
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("123@petrov.com")
    #прикрепляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')         # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций с задержкой в 5 сек
    time.sleep(5)
    browser.quit()