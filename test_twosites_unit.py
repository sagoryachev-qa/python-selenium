from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Testtwosites(unittest.TestCase):

    def setUp(self):
        # Инициализация веб-драйвера перед каждым тестом
        self.browser = webdriver.Chrome()
        
    def test_first(self):
        link1 = "https://suninjuly.github.io/registration1.html"
        self.browser.get(link1)

        input1 = self.browser.find_element(By.TAG_NAME, 'input')
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("petrov@mail.ru")
        input4 = self.browser.find_element(By.CLASS_NAME, "first")
        input4.send_keys("123")
        input5 = self.browser.find_element(By.CLASS_NAME, "second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
                
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1") # находим элемент, содержащий текст
            
        welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_second(self):
        link2 = "https://suninjuly.github.io/registration2.html"
        self.browser.get(link2)

        input1 = self.browser.find_element(By.TAG_NAME, 'input')
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("petrov@mail.ru")
        input4 = self.browser.find_element(By.CLASS_NAME, "first")
        input4.send_keys("123")
        input5 = self.browser.find_element(By.CLASS_NAME, "second")
        input5.send_keys("Russia")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
                
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
            
        welcome_text = welcome_text_elt.text 
        self.assertEqual("Congratulations! You have successfully registered!") == welcome_text
if __name__ == "__main__":
    unittest.main()

                               


    