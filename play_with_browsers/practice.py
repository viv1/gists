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



## cancel load
FirefoxProfile customProfile = new FirefoxProfile();
customProfile.setAcceptUntrustedCertificates(true);
customProfile.setPreference("network.http.connection-timeout", 10);
customProfile.setPreference("network.http.connection-retry-timeout", 10);

driver = new FirefoxDriver(firefox, customProfile);
driver.manage().deleteAllCookies();

##better way to cancel load
WebDriverWait wait = new WebDriverWait(driver, 10);
WebElement element = wait.until(ExpectedConditions.presenceOfElementLocated(By.id(>someid>)));




#################### CAPTCHA ######################

from PIL import Image

img = Image.open('captcha.jpg Your image here!
img = img.convert("RGBA")

pixdata = img.load()

# Make the letters bolder for easier recognition

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
 if pixdata[x, y][0] < 90:
 pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
 if pixdata[x, y][1] < 136:
 pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
 if pixdata[x, y][2] > 0:
 pixdata[x, y] = (255, 255, 255, 255)

img.save("input-black.gifIF")

#   Make the image bigger (needed for OCR)
im_orig = Image.open('input-black.gifig = im_orig.resize((1000, 500), Image.NEAREST)

ext = ".tif"
big.save("input-NEARESTxt)

#   Perform OCR using tesseract-ocr library
from tesseract import image_to_string
image = Image.open('input-NEAREST.tifrint image_to_string(image)