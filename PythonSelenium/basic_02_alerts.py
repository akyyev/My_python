from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


def test1():
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.find_element_by_css_selector('#name').send_keys('John Doe')
    driver.find_element_by_id('alertbtn').click()
    # to handle alerts we need to switch our driver to the alert mode
    # then accept, dismiss, send_keys(), text methods are available
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    
    driver.close()


test1()
