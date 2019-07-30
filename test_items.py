from selenium import webdriver
import time

def test_link_language(test_lang, test_browser):

    link = ("http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(test_lang))
#    print(link)
    test_browser.get(link)
    button = test_browser.find_element_by_class_name("btn-add-to-basket")
#    time.sleep(30)
    assert button
    test_browser.quit()
   
