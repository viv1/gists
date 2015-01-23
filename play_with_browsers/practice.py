from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.fb.com")
# assert "Facebook" in driver.title
elem = driver.find_element_by_name("p")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source


el=driver.find_elemt_by_class_name("_5861 textInput _586g _586p focus_target")
tok="CAACEdEose0cBAKcW1XpFmgmaqYJq7Apwe0dQfmj49HJPKayScxv2eIZCjFQxOjZAE7ZApwsVoQQqtdIjxNZCYuwn1Xar9CpA4tZBGDUYf0dMC0vKKy5Cfv7XUVGdvJU4sowYfRmbXxvj1c4aZCqYUI8smSaNg6k5fTcd9wFpHJqdjAZC3Ez2Oa16ZAR5eZBdjHdliUuPnfAPtUpoYCGJHyU9ZANEdc4c98K3kZD"


driver.find_element_by_link_text("Try Again").click()

time.sleep(1)
for i in range(100):
    driver.find_element_by_class_name("redtile").click()
