import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')

@pytest.fixture(scope="function")

def lang(request):
    br_lang = request.config.option.language
    if br_lang is None:
        pytest.skip()
    return br_lang

@pytest.fixture(scope="function")

def browser(request):
    browser = webdriver.Chrome()
    return browser

