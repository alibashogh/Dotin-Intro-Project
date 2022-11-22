from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from Settings import *


def web_wait(locator, by=By.XPATH, timeout=default_timeout):
    return WebDriverWait(driver, timeout).until(lambda d: driver.find_element(by, locator))


# ********************* Locators ***************************


login_page_button = '//*[@data-cro-id="header-profile"]'
username_field = 'username'
password_field = 'password'
profile_button = '//div[contains(@class, "profileButton")]'
submit_button = '//*[@type="submit"]'
check_username = '//a[@data-cro-id="header-profile-detail"]//span[text()="ali bashogh"]'


driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

web_wait(login_page_button)
driver.find_element(By.XPATH, login_page_button).click()

try:
    web_wait(username_field, By.NAME)
    driver.find_element(By.NAME, username_field).send_keys(username)
    driver.find_element(By.XPATH, submit_button).click()

    web_wait(password_field, By.NAME)
    driver.find_element(By.NAME, password_field).send_keys(password)
    driver.find_element(By.XPATH, submit_button).click()

    web_wait(profile_button)
    driver.find_element(By.XPATH, profile_button).click()
    driver.find_element(By.XPATH, check_username)
except:
    print('Your Login Test Was Failed!')

sleep(3)
driver.quit()
