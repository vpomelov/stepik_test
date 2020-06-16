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

    wait = WebDriverWait(browser, 14)
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    data = browser.find_element_by_id("input_value")
    x = data.text
    Y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(Y)

    button1 = browser.find_element_by_id("solve")
    button1.click()

finally:
    time.sleep(15)
    browser.quit()