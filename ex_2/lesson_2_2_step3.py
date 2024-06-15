from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    #считаем сумму
    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    x = (int(a) + int(b))
    print(x)
    #выбираем то число из списка, которое получилось в "x"
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(x))
    #отправляем данные
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

