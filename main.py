from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
Keys
path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get('https://www.bestbuy.com/site/evga-ko-ultra-gaming-nvidia-geforce-rtx-2060-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6403801.p?skuId=6403801')

print(driver.title)
#print(driver.title) prints the title of the tab within the browser

#time.sleep(3)
#search = driver.find_element_by_id('popup-close')
#search.send_keys(Keys.RETURN)

#time.sleep(5)
#search = driver.find_elements_by_xpath('/html/body/div[7]/div[4]/div[1]/div/a').click()



time.sleep(2)
search = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button').click()  #click add to cart
time.sleep(1)
#search = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div/div/div[3]/button[1]').click()    #click no thanks to purchased protection
#time.sleep(1)
#search = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/button[2]').click()   #click view cart/ go to checkout
#time.sleep(1)
driver.get('http://www.bestbuy.com/cart')
#search = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/div[3]/div[2]/button[1]').click()   #click im not interested in face masks
time.sleep(2)
search = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[2]/button').click()   #click secure checkout
time.sleep(1)
search = driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/form/div[3]/div[1]/div[2]/div[1]/input')
search.send_keys('ericiskooll@gmail.com')
time.sleep(1)

search = driver.find_element_by_name('btnNext').click()
time.sleep(1)
search = driver.find_element_by_name('login_password')
search.send_keys('Password123')
search = driver.find_element_by_name('btnLogin').click()
time.sleep(3)
search = driver.find_elements_by_id('payment-submit-btn')
search.send_keys(Keys.RETURN)
time.sleep(3)

#search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input')
#search.send_keys('ericiskooll@gmail.com')
search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input')
search.send_keys('9095815438')
time.sleep(2)
#search.find_elements_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button')


#search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input')
#search.send_keys('1111222233334444')

#search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[2]/label/div/input')
#search.send_keys('Eric')

#search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[3]/label/div/input')
#search.send_keys('Navarro')

#search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[4]/label/div[2]/div/div/input')
#search.send_keys('123 Main St')

#search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[6]/div/div[1]/label/div/input')
#search.send_keys('Ballsack')

#search = driver.find_element_by_name('state')
#search.send_keys('N'+'N'+'N'+'N'+'N'+'N'+'N').click

#search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[7]/div/div[1]/label/div/input')
#search.send_keys('69696')

#search = driver.find_element_by_name('Phone')
#search.send_keys('9095815438')

#search = driver.find_element_by_name('Email')
#search.send_keys('ericiskooll@gmail.com')

#time.sleep(1)
#driver.get('https://secure.newegg.com/shop/cart')    #go to cart

#time.sleep(1)
#search = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()   #go to checkout

#time.sleep(2)
#search = driver.find_element_by_id('fld-e')
#search.send_keys('ericiskooll@gmail.com')

#search = driver.find_element_by_id('fld-p1')
#search.send_keys('Ericiskoo1')

#search = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button').click()    #click login

#time.sleep(2)
#search = driver.find_element_by_id('consolidatedAddresses.ui_address_2.firstName')
#search.send_keys('Eric')


#time.sleep(3)
#search = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[4]/div/div[2]/button').click()    #continue as guest

#time.sleep(4)
#search = driver.find_element_by_id('firstName').click()
#search.send_keys(Keys.ERIC)

#search = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[2]/label/div/input')
#search.send_keys('Navarro')

#search = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/label/div[2]/div/div/input')
#search.send_keys('531 Lantana Ln')

#search = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[1]/label/div/input')
#search.send_keys('Havelock')

#search = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[6]/div/div[1]/label/div/input')
#search.send_keys('28532')

#search = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input')
#search.send_keys('ericiskooll@gmail.com')

#search = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input')
#search.send_keys('9095815438')
#time.sleep(1)







#driver.quit()
#driver.quit()     closes the browser
#driver.close()    closes the tab