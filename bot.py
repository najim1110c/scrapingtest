

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from twilio.rest import Client
import requests
from twilio.rest import Client
import tkinter as tk
import time


class Bot:
    def __init__(self, name):
        self.name = name

    def print_hi(self):

        print(f'Hi, {self.name}')  # Press Ctrl+F8 to toggle the breakpoint.

        # SHURU
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get("https://ebusiness.avma.org/ecfvg/avmacertificationmain.aspx")
        driver.get("https://ebusiness.avma.org/ECFVG/ECFVGlogin.aspx")
        # element = driver.find_element(By.ID,"btnYes")#.send_keys(Keys.ENTER)
        element = driver.find_element(By.ID, "txtUserID")  # .send_keys(Keys.ENTER)

        # element = driver.find_element_by_name("C005$Wizard1$btnYes")
        # time.sleep(5)
        element.click()
        element.send_keys("Ebada1993usa@gmail.com")
        # print(element)
        time.sleep(1)
        element = driver.find_element(By.ID, "txtPassword")  # .send_keys(Keys.ENTER)
        element.click()
        element.send_keys("1411245245Aa@")
        time.sleep(1)
        element = driver.find_element(By.ID, "ctl12_cmdLogin")  # .send_keys(Keys.ENTER)
        element.click()
        time.sleep(2)
        driver.get("https://ebusiness.avma.org/ECFVG/AVMACPESchedule.aspx?ID=8085")
        time.sleep(1)
        print("first table")
        table = driver.find_element(By.ID, "C003_dlv_rblExamDate_0")
        time.sleep(1)
        print(table.text)
        time.sleep(1)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        print(len(rows))
        if len(rows) > 3:
            account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
            auth_token = '6632d9f1530b0b2f49c5a7f62f0e68b0'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='New Exam Schedule found ',
                to='whatsapp:+8801816633106'
            )
            print(message.sid)
        for i in range(0, len(rows)):
            table = driver.find_element(By.ID, "C003_dlv_rblExamDate_0")
            # print(table2.text)
            time.sleep(2)
            rows = table.find_elements(By.TAG_NAME, 'tr')
            # print(i)
            print(rows[i].text)
            rows[i].click()
            time.sleep(2)
            finalTable = driver.find_element(By.ID, "grdSectionInfo")
            # td = driver.find_element_by_xpath('//*[@id="grdSectionInfo"]/tbody/tr[2]/td[2]')
            td = driver.find_element("xpath", '//*[@id="grdSectionInfo"]/tbody/tr[2]/td[2]')
            print("allin one " + finalTable.text)
            print("only available seat " + td.text)
            convertNumber = int(td.text)
            print(convertNumber)
            if (convertNumber > 0):
                account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
                auth_token = '6632d9f1530b0b2f49c5a7f62f0e68b0'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='available seat is 0 ',
                    to='whatsapp:+8801816633106'
                )
                print(message.sid)
            else:
                pass
            time.sleep(2)

        print("second table")
        table2 = driver.find_element(By.ID, "C003_dlv_rblExamDate_1")
        time.sleep(1)
        print(table2.text)
        time.sleep(1)
        rows = table2.find_elements(By.TAG_NAME, 'tr')
        print("here starts tag")
        print(len(rows))
        if len(rows) > 7:
            account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
            auth_token = '6632d9f1530b0b2f49c5a7f62f0e68b0'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='New Exam Schedule found ',
                to='whatsapp:+8801816633106'
            )
            print(message.sid)
        # print(rows[2].text)
        # rows[2].click()
        # time.sleep(5)
        print("here starts tag")
        for i in range(0, len(rows)):
            table2 = driver.find_element(By.ID, "C003_dlv_rblExamDate_1")
            # print(table2.text)
            time.sleep(2)
            rows = table2.find_elements(By.TAG_NAME, 'tr')
            # print(i)
            print(rows[i].text)
            rows[i].click()
            time.sleep(2)
            finalTable = driver.find_element(By.ID, "grdSectionInfo")
            # td = driver.find_element_by_xpath('//*[@id="grdSectionInfo"]/tbody/tr[2]/td[2]')
            td = driver.find_element("xpath", '//*[@id="grdSectionInfo"]/tbody/tr[2]/td[2]')
            print("allin one " + finalTable.text)
            print("only available seat " + td.text)
            convertNumber = int(td.text)
            print(convertNumber)
            if (convertNumber > 0):
                account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
                auth_token = '6632d9f1530b0b2f49c5a7f62f0e68b0'
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='available seat is 0 ',
                    to='whatsapp:+8801816633106'
                )
                print(message.sid)
            else:
                pass
            time.sleep(2)

        # for row in rows:
        #    print(row)
        # row.click()
        # time.sleep(2)
        driver.close()

        print("shesh")