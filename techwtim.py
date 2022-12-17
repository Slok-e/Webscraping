from selenium import webdriver

# I reccomend changing the web driver location to your program(x86)folder (Windows) or /Library/ (Mac) or somewhere you can easily allocate.
PATH = "/Library/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")