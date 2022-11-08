import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import Select

# waiting time between actions
WAIT_TIME = 1.5

# open chrome and amazon.com

driver = webdriver.Chrome('C:\ichig\eclipse-workspace\Selenium\chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")


# look up the text box
textbox = driver.find_element(By.ID, "twotabsearchtextbox")
sleep(WAIT_TIME)
# write HP Pavilion azul
textbox.send_keys("HP Pavilion azul")
# press enter
textbox.send_keys("\n")

sleep(WAIT_TIME)

# select first item
driver.find_element(
    By.CSS_SELECTOR, ".s-main-slot .s-list-col-right h2 .a-link-normal").click()
sleep(WAIT_TIME)
sleep(5)
