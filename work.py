from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


'''
print("请输入uis用户名") 
usrname = input()
print("请输入uis密码")
password = input()
'''

usrname = '*****'
password = '***'

driver = webdriver.Chrome()
url = "http://ce.fudan.edu.cn"
from selenium.webdriver.common.by import By
driver.get(url)
usr = driver.find_element(By.ID, 'username')
pwd = driver.find_element(By.ID, 'password')
submit = driver.find_element(By.ID, 'idcheckloginbtn')


usr.send_keys(usrname)   #填入uis用户名
pwd.send_keys(password)   #填入uis密码

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

submit.click()

while True:
    driver.get("http://ce.fudan.edu.cn/")
    
    # Click on the element with class 'evaluateMyTask'
    driver.find_element(By.CLASS_NAME, 'evaluateMyTask').click()
    time.sleep(1)
    
    # Switch to the iframe
    driver.switch_to.frame("iframepage")
    
    # Find the first clickable link
    a = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#tblQuestion > tbody > tr:nth-child(1) > td.operate > a'))
    )
   
    a.click()
    time.sleep(2)
    
    # Switch to the newly opened window
    driver.switch_to.window(driver.window_handles[1])
    
    # Find all radio button wrappers
    radios = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'jqTransformRadioWrapper'))
    )

    
    # Find all checkbox wrappers
    checkboxes  = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'jqTransformCheckboxWrapper'))
)

    
    # Click on all displayed radio buttons in reverse order
    n=0
    for i in reversed(radios):
        n+=1
        if n >32 and n <=35 :
            continue
            
        if i.is_displayed():
            i.click()
            
    
    # Click on the first 8 displayed checkboxes and last question's checkbox
    cnt = 0
    for i in checkboxes:
        if i.is_displayed():
            cnt += 1
            i.click()
        if cnt >= 8:
            break
    cnt = 0 
    for i in checkboxes:
        if i.is_displayed():
            cnt += 1
            
        if cnt == 20:
            i.click()
            break
    # Find all text areas and fill them with "好"
    textareas = driver.find_elements(By.TAG_NAME, 'textarea')
    for i in textareas:
        i.send_keys('好')


    # Click the button with id 'next_button'
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'next_button'))
    )
    button.click()
    
    # Find all buttons and click the one with data-id='ok'
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for i in buttons:
        if i.get_attribute('data-id') == 'ok':
            print('here')
            i.send_keys(Keys.ENTER)
    
    # Close the current window
    driver.close()
    # Switch back to the main window
    driver.switch_to.window(driver.window_handles[0])