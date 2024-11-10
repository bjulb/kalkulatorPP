from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://cennik.poczta-polska.pl/usluga,krajowy_pocztex.html")

driver.implicitly_wait(2)

driver.quit()