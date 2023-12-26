import random
import time
import allure
from allure_commons.types import AttachmentType
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#new comments added here

def test_tutorials_ninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    # ele = driver.find_element(By.ID,"//input[@id='button-search']")

    try:
        # A URL that delays loading
        driver.get("https://tutorialsninja.com/demo/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='input-search']").send_keys("HP")
        time.sleep(2)
        # ele =driver.find_element(By.XPATH,"//input[@id='button-search']")
        wait = WebDriverWait(driver,10)
        ele = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='button-search']")))
        ele.click()
        driver.get_screenshot_as_file("C:\\Users\\shashi\\PycharmProjects\\Pycharm_ECOM\\Screenshots_new\\ss111.png")
        expected_text = "HP LP306"
        actual_text =driver.find_element(By.XPATH,"//a[text()='HP LP3065']")
        if actual_text.__eq__(expected_text):
            print("PASSED !!!!")

    except Exception as err:
        print("exception is :",err)

    finally:
        # else quit
        driver.quit()


