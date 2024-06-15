from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    #инициализируем браузер
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    #жмякаем кнопочку
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    #вносим полученное значени в поле для ответа
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    #отправляем данные
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # закрываем браузер после всех манипуляций с задержкой в 5 сек
    time.sleep(5)
    browser.quit()