from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os
import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)
    
    # Нажимаем на кнопку
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Переходим на окошко confirm
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # Считываем x и считаем y
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(int(x_element))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    # Отправляем ответ
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    #закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()