from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем x и считаем y
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(int(x_element))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    # Скроллим до видимости кнопки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # Проставляем галочки в чекбокс и радиобаттон
    option = browser.find_element(By.CSS_SELECTOR, "#robotcheckbox")
    option.click()
    robot1 = browser.find_element(By.CSS_SELECTOR, "#robotsrule")
    robot1.click()
    
    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()