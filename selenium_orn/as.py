from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://facebook.com")
# //*[@id="u_0_2"]
time.sleep(10)
giris_yap = driver.find_element_by_xpath('//*[@id="u_0_2"]')
ad = driver.find_element_by_xpath('//*[@id="email"]')
ad.send_keys('iletisim@sinanurun.com')
# giris_yap.click()
sifre = driver.find_element_by_xpath('//*[@id="pass"]')
sifre.send_keys('**********')
giris_yap.click()
time.sleep(10)
gruplar = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div[3]/div[3]/ul/li[1]/a/span/i')
gruplar.click()
time.sleep(10)
g1 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/div[2]/ul/li[1]/ul/li[1]/div/div/div[1]/img')
g1.click()
time.sleep(10)
ilk = driver.get('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div')
ilk.send_keys("merhaba")
time.sleep(10)
gonder = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div[3]/div/div[2]/div/div[2]/span/button')
gonder.click()
time.sleep(10)
driver.close()