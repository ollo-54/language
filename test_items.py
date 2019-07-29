from selenium import webdriver
import time

def test_link(lang, browser):

    link = ("http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(lang))
#    print(link)
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
#    time.sleep(30)
    assert button
    browser.quit()
   
