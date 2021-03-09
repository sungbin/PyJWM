from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'/home/sb/gdriver/geckodriver')

driver.get('http://inventwithpython.com')
