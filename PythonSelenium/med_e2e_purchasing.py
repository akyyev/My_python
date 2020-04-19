from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


def test1():
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    # product_names = driver.find_elements_by_css_selector("h4.card-title a")
    products = driver.find_elements_by_xpath("//div[@class='card h-100']")

    # products   = //div[@class='card h-100']
    # blackberry = //div[@class='card h-100']/div/h4/a
    # add_button = //div[@class='card h-100']/div[2]/button
    for product in products:
        if product.find_element_by_xpath('div/h4/a').text == 'Blackberry':
            print(product.find_element_by_xpath('div/h4/a').text)
            # adding item to the cart
            product.find_element_by_xpath('div[2]/button').click()
    # let's click check out
    driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    # another checkout button
    driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    # selecting delivery location
    driver.find_element_by_id('country').send_keys('ind')

    # wait is needed for suggestion
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element_by_link_text('India').click()

    # clicking on checkbox for agreement
    driver.find_element_by_css_selector("label[for='checkbox2']").click()

    # submit button
    driver.find_element_by_css_selector("[type='submit']").click()

    # confirmation message
    conf_message = driver.find_element_by_xpath("//div[contains(@class, 'alert-dismissible')]").text

    print(conf_message)
    assert 'Success! Thank you!' in conf_message

    driver.get_screenshot_as_file('screen.png')
    driver.close()


test1()
