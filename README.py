# Edu phyton_tests
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://mail.ru/')
driver.find_element_by_xpath("//*[@id='mailbox']/div[1]/a").click()
#webdriver.findElement(By.xpath("/html/body/main/div[1]/div[1]/div/div/div[1]/a[3]")).click()
assert "mail" in driver.page_source
driver.quit()