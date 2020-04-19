import random

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


def test1():
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    # input[type='checkbox']
    checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
    print(f'There are {len(checkboxes)} checkboxes.')

    for box in checkboxes:
        box.click()

    # choice = random.choice(checkboxes)
    # choice.click()
    # sleep(3)
    # print('Choice 1 is unchecked!')
    # try:
    #     assert checkboxes[0].is_selected()
    #     print('Checkbox 1 is selected')
    # except AssertionError:
    #     print('Random choice was 1')

    for box in checkboxes:
        if box.get_attribute('value') == 'option2':
            box.click()
            print('Option2 is not selected')
            sleep(2)

    driver.close()
