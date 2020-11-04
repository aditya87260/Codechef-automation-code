[5:35 PM, 9/1/2020] +91 96503 87926: import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions


browser=webdriver.Chrome("/Users/stutijain/Downloads/chromedriver")
browser.get("https://codechef.com")
username_element=browser.find_element_by_id("edit-name")
username_element.send_keys("stutijain578")
password_element=browser.find_element_by_id("edit-pass")
from getpass import getpass
password_element.send_keys(getpass("enterpassword"))
browser.find_element_by_id("edit-submit").click()
[5:35 PM, 9/1/2020] +91 96503 87926: with open("/Users/stutijain/Downloads/Ide.cpp",'r') as f:
    code=f.read()
    
browser.get("https://www.codechef.com/submit/RGAME")


time.sleep(5)
browser.find_element_by_id("edit-submit").click()


browser.execute_script("window.scrollTo(0, 700)") 
time.sleep(5)
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

#If internet connection is slow, uncomment next line
# time.sleep(10)

browser.execute_script("window.scrollTo(0, 500)") 
prog_input=browser.find_element_by_id("edit-program")
prog_input.send_keys(code)

#If internet connection is slow, uncomment next line
# time.sleep(10)

browser.execute_script("window.scrollTo(0, 600)") 
browser.find_element_by_id("edit-submit-1").click()