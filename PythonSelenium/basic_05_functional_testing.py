from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


# Verify products are same on both select page and summary page
def test1():
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys('ber')
    sleep(1)
    buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
    products = []
    for each in buttons:
        # we can traverse up by using current element
        # //div[@class='product-action']/button/parent::div/parent::div/h4
        # only last part is necessary --> parent::div/parent::div/h4
        products.append(each.find_element_by_xpath('parent::div/parent::div/h4').text)
        each.click()
    # so we don't need another for loop...
    # products = [each.text for each in driver.find_elements_by_css_selector('h4.product-name')]
    print('Products before: ', products)

    driver.find_element_by_css_selector("img[alt='Cart']").click()
    driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

    #                                                                                    just to remove empty ones
    productsAfter = [each.text for each in driver.find_elements_by_css_selector("p.product-name") if each.text]
    print('Products after: ', productsAfter)
    assert products == productsAfter

    # explicit wait
    wait = WebDriverWait(driver, 10)
    # this part is important, make sure you use By class and put it in () with value
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))
    driver.find_element_by_class_name('promoCode').send_keys('invalidPromoCode')
    driver.find_element_by_class_name('promoBtn').click()

    # this is also needs to be handled, 5 second wasn't enough so, I changed it to 10
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'span.promoInfo')))
    print(driver.find_element_by_css_selector("span.promoInfo").text)
    driver.close()


# verify promo code is applied when valid promo is entered
def test2():
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
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='totAmt']")))
    original_amount = float(driver.find_element_by_xpath("//span[@class='discountAmt']").text)

    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))
    driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
    driver.find_element_by_class_name('promoBtn').click()
    driver.find_element_by_class_name('promoBtn').click()

    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'span.promoInfo')))
    print(driver.find_element_by_css_selector("span.promoInfo").text)

    discounted_amount = float(driver.find_element_by_xpath("//span[@class='discountAmt']").text)
    print('Before: ', original_amount)
    print('After: ', discounted_amount)
    assert discounted_amount == original_amount * (1 - 10 / 100)
    driver.close()


# verify total amount is correct
def test3():
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys('ber')
    sleep(1)
    buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
    for each in buttons:
        each.click()
    driver.find_element_by_css_selector("img[alt='Cart']").click()
    driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='discountAmt']")))
    amount = float(driver.find_element_by_xpath("//span[@class='discountAmt']").text)

    prices = [float(each.text) for each in driver.find_elements_by_xpath("//tr/td[5]/p")]
    assert amount == sum(prices)
    driver.close()


# Verify search functionality is working
# input: ber
# Req: 3 products, names = x, y, z
def test4():
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys('ber')
    sleep(1)
    buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
    products = []
    for each in buttons:
        each.click()
    products = [each.text for each in driver.find_elements_by_css_selector('h4.product-name')]
    exp = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
    assert exp == products
    driver.close()


test4()
