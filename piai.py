from time import sleep  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By  
import warnings  
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import os
warnings.simplefilter("ignore")  
 
warnings.simplefilter("ignore")
url = "https://pi.ai/talk"
os.environ['PATH'] = r"c:\SeleniumDrivers"
chrome_options = Options()
chrome_options.add_argument("--headless=new") #Runs chrome without gui 
chrome_options.add_argument('--log-level=3')# helps not to print useless arguments by the selenium
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)

def Clicker():
    driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/button").click()
    sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/button").click()
    sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[2]/div[2]/button[2]").click()

def Model6(Query):
    try:
        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/button").click()
        sleep(1)
        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/button").click()
        sleep(1)
        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[1]/div[2]/button[2]").click()
        sleep(2)
    
    except:
        pass

    Query = str(Query)  
    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea").send_keys(Query)  
    sleep(3)  
    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click() 
    sleep(0.01)

    while True:  
  
        sleep(30)  
          
        try:  
            AnswerXpath = "/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]"  
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()  
            if str(Answer)=="True":  
                break    
        except:  
            pass   

    AnswerXpath = f"/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]"  
      
    Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text  
     
    return Answer  

while True:  
          
        Query = input("Enter Your Query : ")  
        answer = Model6(Query)  
        print(answer) 
        try:
            if "bye" in Query:
                sleep(8)
                driver.quit()
                sys.exit()
            else:
                    pass

        except Exception as e:
                print(e)

