from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    
    
    browser.get("http://suninjuly.github.io/cats.html")
    button = browser.find_element(By.ID, "button")

finally:
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()