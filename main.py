# This is a sample Python script.

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
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    '''
    account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
    auth_token = '8407867db5c587e8cdd7ded28d9929c1'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your appointment is coming up on July 21 at 3PM',
        to='whatsapp:+8801816633106'
    )

    print(message.sid)
    '''
    # print("shesh")

    # x = requests.get('https://nodecloths.com')
    # print(x.text)
    #SHURU
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
        auth_token = '8407867db5c587e8cdd7ded28d9929c1'
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
            auth_token = '8407867db5c587e8cdd7ded28d9929c1'
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
        auth_token = '8407867db5c587e8cdd7ded28d9929c1'
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
            auth_token = '8407867db5c587e8cdd7ded28d9929c1'
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
    '''
    account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
    auth_token = '8407867db5c587e8cdd7ded28d9929c1'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='All Scraping has finished and this a whatsapp notification ',
        to='whatsapp:+8801816633106'
    )

    print(message.sid)
    '''
    print("shesh")





import time
import threading
from tkinter import *
root = Tk()
root.title("Loop Terminate")
root.geometry("400x400")

time.sleep(0.5)

stop = False
label = Label(root, text="")
def button_stop_command():
  # If the STOP button is pressed then terminate the loop
  global stop
  stop = True
  account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
  auth_token = '8407867db5c587e8cdd7ded28d9929c1'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
      from_='whatsapp:+14155238886',
      body='stoed',
      to='whatsapp:+8801816633106'
  )
  label.config(text="stopped")

  print(message.sid)

def button_start_command():
  global stop
  stop = False
  j = 1
  account_sid = 'AC4a32ce8cc378d257f6fd84c64a87c2f2'
  auth_token = '8407867db5c587e8cdd7ded28d9929c1'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
      from_='whatsapp:+14155238886',
      body='started',
      to='whatsapp:+8801816633106'
  )
  label.config(text="started")
  label.config(text="running")

  print(message.sid)
  while not stop:
    print("Loop Index = " + str(j))
    j = j+1
    time.sleep(3)
    print_hi('PyCharm')
    time.sleep(10)

def button_starter():
  t = threading.Thread(target=button_start_command)
  t.start()

# Button START
button_start = Button(root, text="START", padx=30, pady=20, command=button_starter)
button_start.grid(columnspan=1, row=1,column=0)

# Button STOP
button_stop = Button(root, text="STOP", padx=33, pady=20, command=button_stop_command)
button_stop.grid(row=2, column=0)




label.grid(row=3,column=0)
root.mainloop()







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
