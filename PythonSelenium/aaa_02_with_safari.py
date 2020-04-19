from selenium import webdriver

driver = webdriver.Safari()


# for firefox, and ie download dedicated webDrivers
def run():
    driver.maximize_window()
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


run()
