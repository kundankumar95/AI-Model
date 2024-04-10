from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re
import os
warnings.simplefilter("ignore")
url = "https://chat-app-b8c333.zapier.app/zapchat"
os.environ['PATH'] = r"c:\SeleniumDrivers"
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument('--log-level=3')
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)

Chat_Num = 2


def SecurityByPass():
    while True:
        website_title = driver.title
        if "just a moment" in str(website_title).lower():
            driver.refresh()
            sleep(3)
        else:
            break


def Query(Query):
    Query = str(Query).lower()
    try:
        TextBox = driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/main/div[1]/div/div/div/div/div/div/div/form/fieldset/textarea")
        TextBox.send_keys(Query)

    except Exception as e:
        print(e)
    sleep(0.5)

    try:
        driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/main/div[1]/div/div/div/div/div/div/div/form/fieldset/button").click()

    except:
        driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/main/div[1]/div/div/div/div/div/div/div/form/fieldset/button").click()


def Result():
    global Chat_Num
    Chat_Num = str(Chat_Num)
    XpathValue = f"/html/body/div[1]/main/div[1]/div/div/div/div/div/div/div/div/div/div[{Chat_Num}]/div[2]"
    try:
        Text = driver.find_element(by=By.XPATH, value=XpathValue).text
        print(Text)

    except Exception as e:
        print(e)

    Chat_NumNew = int(Chat_Num) + 1
    Chat_NumNew = str(Chat_NumNew)
    Chat_Num = Chat_NumNew


def Model11(Data):
    SecurityByPass()
    Query(Query=Data)
    sleep(10)
    Result()

while True:
    a = input("Enter your query : ")
    Model11(Data=a)
