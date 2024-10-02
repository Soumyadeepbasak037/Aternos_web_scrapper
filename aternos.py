from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pywhatkit
service = Service(executable_path='./geckodriver.exe')
profile_path = "C:\\Users\\Soumyadeep.DESKTOP-HN2SUP0\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\vqv0wjbz.default-release"

options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
options.add_argument("--headless")
# options.add_argument("--disable-blink-features")
# options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Firefox(service=service, options=options)
headers={'User-Agent': 'Mozilla/5.0'}

try:
    driver.get("https://aternos.org/server/")
    time.sleep(5)
    # start_btn = driver.find_element(By.XPATH, "//div[@id='start']")
    # time.sleep(2)
    # start_btn.click()
    # time.sleep(2)
    i = 0
    # print(driver.page_source)
    # flag = True
    while(True):
        time.sleep(5)
    
        status = driver.find_element(By.CLASS_NAME, "statuslabel-label")
    
        # time.sleep(5)
        
        queue_left = driver.find_element(By.XPATH, '//*[@class="server-status-label-right queue-position"]')
        
        print(status.text)
        print(queue_left.text)
        
        my_queue = queue_left.text.split("/")
        required = my_queue[0]
        # print(required)
        
        required_int =  int(required)
        
        print(required_int)
        confirm_btn = driver.find_element(By.XPATH, '//*[@class="btn btn-huge btn-success btn-clickme"]')
        if(required_int == 1):
            print("Time to Click")
            confirm_btn.click()
        #<div id="confirm" class="btn btn-huge btn-success btn-clickme"><i class="fas fa-check-square"></i>Confirm now!</div> -- confirm button

finally:
    driver.quit()
    







    
# driver.get("https://aternos.org/server/")
# time.sleep(20)
# driver.quit()
# username_field  = driver.find_element(By.CLASS_NAME, "username")
# password_field = driver.find_element(By.CLASS_NAME, "password")
# # login_button = driver.find_element(By.CLASS_NAME, "login-button btn btn-main join-left")
# login_button = driver.find_element(By.XPATH, "//button[@title='Login']")
# time.sleep(3)
# username_field.send_keys("hydrogen_test")
# time.sleep(2)
# password_field.send_keys("amarNamPuku")
# time.sleep(5)
# login_button.click()


