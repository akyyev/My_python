from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


# Waits:
#   Implicit
#   Explicit
#   Pause the test using sleep method (python)


# explicit wait --> it's for only targeted element, there are conditions we can use.


def test1():
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys('ber')
    sleep(1)
    buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
    for each in buttons:
        each.click()
    driver.find_element_by_css_selector("img[alt='Cart']").click()
    driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
    # explicit wait
    wait = WebDriverWait(driver, 10)
    # this part is important, make sure you use By class and put it in () with value
    wait.until(expected_conditions.presence_of_element_located(   (By.CLASS_NAME, 'promoCode')  ))
    driver.find_element_by_class_name('promoCode').send_keys('invalidPromoCode')
    driver.find_element_by_class_name('promoBtn').click()

    # this is also needs to be handled, 5 second wasn't enough so, I changed it to 10
    wait.until(expected_conditions.presence_of_element_located(   (By.CSS_SELECTOR, 'span.promoInfo')   ))
    print(driver.find_element_by_css_selector("span.promoInfo").text)
    driver.close()


# def test2():
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://google.com/ncr")
#     driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
#     first_result = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='ed_6']")))
#     print(first_result.get_attribute("textContent"))


test1()
