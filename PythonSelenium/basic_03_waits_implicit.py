from time import sleep

from selenium import webdriver

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')

# Waits:
#   Implicit
#   Explicit
#   Pause the test using sleep method (python)


# implicit wait --> wait until 5 seconds if object is not displayed
# global wait
# let's say 1.5 seconds was enough to get object, then it will wait only 1.5 seconds not 5 seconds
# if object never shows up it will raise NoSuchElementException
driver.implicitly_wait(5)


def test1():
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys('ber')
    sleep(1)
    buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
    for each in buttons:
        each.click()
    driver.find_element_by_css_selector("img[alt='Cart']").click()
    driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
    driver.find_element_by_class_name('promoCode').send_keys('invalidPromoCode')
    driver.find_element_by_class_name('promoBtn').click()
    print(driver.find_element_by_css_selector("span.promoInfo").text)


test1()
