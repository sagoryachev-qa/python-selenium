from selenium import webdriver
from selenium.webdriver.common.by import By

def test_first(): # инициализируем функцию для pytest
    link1 = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("petrov@mail.ru")
    input4 = browser.find_element(By.CLASS_NAME, "first")
    input4.send_keys("123")
    input5 = browser.find_element(By.CLASS_NAME, "second")
    input5.send_keys("Russia")

     # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
                
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1") # находим элемент, содержащий текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text 
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


def test_second(): #инициализируем функцию для второго сайта
    link2 = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link2)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("petrov@mail.ru")
    input4 = browser.find_element(By.CLASS_NAME, "first")
    input4.send_keys("123")
    input5 = browser.find_element(By.CLASS_NAME, "second")
    input5.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
                
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            
    welcome_text = welcome_text_elt.text 
    assert"Congratulations! You have successfully registered!" == welcome_text


                               


    