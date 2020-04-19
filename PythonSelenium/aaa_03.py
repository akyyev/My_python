from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import Select

from time import sleep

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


def verify(exp, act):
    try:
        assert exp == act
    except AssertionError:
        print("Expected: {} \nFound: {}".format(exp, act))


# for firefox, and ie download dedicated webDrivers
def test():
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # assertion to verify page title
    try:
        assert driver.title == 'ProtoCommerce'
    except AssertionError as e:
        print('Title is not correct', e)

    driver.find_element_by_name('name').send_keys('John')
    email = driver.find_element_by_name('email')
    email.clear()
    email.send_keys('doe@gmail.com')

    driver.find_element_by_css_selector("input[type='password']").send_keys('hello123')
    driver.find_element_by_id("exampleCheck1").click()
    driver.find_element_by_css_selector("input[type='submit']").click()

    assert 'Success!' in driver.find_element_by_xpath("//div[contains(@class, 'alert alert-success')]").text

    # select class provide the methods to handle the options in dropDown
    drop_down = Select(driver.find_element_by_id('exampleFormControlSelect1'))
    drop_down.select_by_visible_text('Male')
    sleep(1)
    drop_down.select_by_index(1)
    sleep(1)
    driver.close()


# to handle dynamic drop-down menu
def test2():
    driver.get('https://www.makemytrip.com')
    driver.find_element_by_xpath("//span[contains(text(),'From')]").click()
    driver.find_element_by_xpath("//input[contains(@placeholder,'From')]").send_keys('del')

    sleep(3)
    cities = driver.find_elements_by_css_selector("p[class*='appendBottom5 blackText']")
    print(len(cities))
    try:
        for city in cities:
            if city.text == 'Indore, India':
                city.click()
    except StaleElementReferenceException:
        print('----------------')

    driver.find_element_by_xpath("//p[text()='Delhi, India']").click()
    sleep(3)
    driver.close()


# to handle checkboxes
def test3():
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    # input[type='checkbox']
    ls = driver.find_elements_by_xpath("//input[contains(@id, 'checkBox')]")
    for i in ls:
        i.click()
    sleep(4)
    driver.close()





