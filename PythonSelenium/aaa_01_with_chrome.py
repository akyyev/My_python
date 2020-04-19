from selenium import webdriver
# 1. pip install selenium
# 2. driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')
driver.maximize_window()


def sel():
    driver.get("https://www.google.com")

    print(driver.title)
    print(driver.current_url)
    # assertion to verify page title
    try:
        assert driver.title == 'Googles'
    except AssertionError as e:
        print('Title is not correct', e)

    driver.get('https://www.amazon.com')

    driver.back()
    driver.refresh()

    driver.quit()


sel()
