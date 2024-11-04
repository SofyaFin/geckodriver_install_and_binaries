from selenium import webdriver
from geckodriver_py import binary_path  # this will get you the path variable

svc = webdriver.FirefoxService(executable_path=binary_path)
driver = webdriver.Firefox(service=svc)
driver.get("http://www.python.org")
assert "Python" in driver.title
