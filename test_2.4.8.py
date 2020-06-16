from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:

    wait = WebDriverWait(browser, 14) #объявление ожидания в 14 секунд
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #будем ждать пока сумма не станет 100 долларов
    button = browser.find_element_by_id("book") #находим кнопку
    button.click() #жмем на кнопку

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x))))) #формула для вычисления

    data = browser.find_element_by_id("input_value") #объявление поля с данными X
    x = data.text #вытягивем данные из Х в виде текста
    Y = calc(x) #вычисление

    answer = browser.find_element_by_id("answer") 
    answer.send_keys(Y)

    button1 = browser.find_element_by_id("solve")
    button1.click()

finally:
    time.sleep(15)
    browser.quit()