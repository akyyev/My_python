# HTML DOM document
# The document object represents your web page
# JS DOM can access any elements on web page just like how selenium does
# selenium have a method to execute JS code in it

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


# JS example (document.getElementsByCss, xpath, name, ...)
def test1():
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    name = driver.find_element_by_name("name")
    name.send_keys("hello")
    print(name.text)  # it won't work
    print(name.get_attribute('value'))
    print(driver.execute_script("return document.getElementsByName('name')[0].value"))

    shop_button = driver.find_element_by_xpath("//a[contains(text(),'Shop')]")
    driver.execute_script("arguments[0].click();", shop_button)

    # scrolling down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    driver.quit()


test1()
