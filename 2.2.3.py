from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем два числа
    x_element = browser.find_element(By.CSS_SELECTOR, '#num1').text
    y_element = browser.find_element(By.CSS_SELECTOR, '#num2').text
    answer = int(x_element) + int(y_element)
    
    # Выбираем правильное значение в списке
    select = Select(browser.find_element(By.CSS_SELECTOR, 'select'))
    select.select_by_visible_text(str(answer))
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()