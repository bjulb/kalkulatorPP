import pytest
from selenium import webdriver

def test_first(ffx_browser):
    ffx_browser.get("https://cennik.poczta-polska.pl/usluga,krajowy_pocztex.html")
    ffx_browser.implicitly_wait(2)
    print("okej, załadowane")
    ffx_browser.quit()