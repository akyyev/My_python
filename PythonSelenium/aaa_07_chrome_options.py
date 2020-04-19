from time import sleep
from selenium import webdriver

# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver',
                          options=chrome_options)


# JS example (document.getElementsByCss, xpath, name, ...)
def test1():
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    print(driver.title)
    driver.quit()


test1()
