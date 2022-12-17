from selenium import webdriver

PATH = "/Library/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://beli.cleverapps.io/api/rank-list/7b002fa2-74dd-4478-a923-366223e67486/")