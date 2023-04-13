from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def func1():
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements(By.CSS_SELECTOR,".form-control")
        for i in elements:
            i.send_keys("FFF")


        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        print(welcome_text)

        return welcome_text

assert "Congratulations! You have successfully registered!" == func1()

