from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('/Users/mac/PycharmProjects/My_python_project/PythonSelenium/chromedriver')


# Handling multiple tabs
def test1():
    driver.get('https://the-internet.herokuapp.com/windows')
    driver.find_element_by_xpath("//a[contains(text(),'Click Here')]").click()
    ls = driver.window_handles
    driver.switch_to.window(ls[1])
    print(driver.find_element_by_tag_name('h3').text)
    driver.close()

    sleep(1)
    driver.switch_to.window(ls[0])
    print(driver.find_element_by_tag_name('h3').text)
    driver.quit()  # quit will browser, but close will close the tab


# Handling iFrames (html doc inside html document, nested)
# iFrame, frameSet, frame
def test2():
    driver.get('https://the-internet.herokuapp.com')
    driver.find_element_by_link_text('Frames').click()
    driver.find_element_by_link_text('iFrame').click()

    # pass frame id or index value
    driver.switch_to.frame("mce_0_ifr")
    text_box = driver.find_element_by_css_selector("#tinymce>p")
    text_box.clear()
    text_box.send_keys("I am able to automate with python")
    sleep(1)
    # this won't work
    # text method can't get whatever you input
    # so use JS executor
    print('Text box: ', text_box.text)

    driver.switch_to.default_content()
    print('After switching frame back to base frame: ', driver.find_element_by_tag_name("h3").text)

    driver.quit()


test2()
