import pytest
from pytest import fixture
from selenium import webdriver

@fixture(scope="function")
def ffx_browser():
    browser = webdriver.Firefox()
    return browser