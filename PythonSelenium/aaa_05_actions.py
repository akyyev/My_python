from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


# Action chains
# hover over example
def test1():
    driver.get('https://www.amazon.com')
    # Action chains class to automate mouse pointer
    action = ActionChains(driver)
    # .build() is used if you perform multiple actions
    # don't forget to add perform() method at the end, IMPORTANT
    sleep(1)
    action.move_to_element(driver.find_element_by_xpath("//a[@id='nav-link-accountList']")).perform()
    action.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'Your Orders')]")).click().perform()
    print(driver.title)
    driver.quit()


# double click example
def test2():
    driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
    # Action chains class to automate mouse pointer
    action = ActionChains(driver)
    action.double_click(driver.find_element_by_id("double-click")).perform()
    alert = driver.switch_to.alert
    sleep(2)
    assert alert.text == 'You double clicked me!!!, You got to be kidding me'
    alert.accept()
    driver.quit()


def test3():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    


test2()
