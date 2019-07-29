from selenium import webdriver

def test_guest_should_see_login_link(lang, browser):

    link = ("http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(lang))
#    print(link)
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button
    browser.quit()
   
