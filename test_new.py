
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest



def test_func11():
        link1 = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
        for i in elements:
            i.send_keys("FFF")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

def test_func1():
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
        for i in elements:
            i.send_keys("FFF")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text= welcome_text_elt.text



        assert "Congratulations! You have successfully registered3!" == welcome_text






