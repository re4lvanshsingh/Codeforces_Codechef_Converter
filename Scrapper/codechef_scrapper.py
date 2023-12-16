from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()

driver.get('https://www.codechef.com/contests/')
elements = WebDriverWait(driver, 50).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._dark_1c9os_272:nth-child(2) ._start-date__container_1c9os_388 p , ._dark_1c9os_272:nth-child(2) span'))
    )
i=0
contests=[]
for element in elements:
    if(i==2):
        contest['time']=element.text
        contests.append(contest)
        i=0
        continue
    if(i==1):
        contest['date']=element.text
        i=i+1
        continue
    if(i==0):
        contest={}
        contest['name']=element.text
        i=i+1
with open('csv/contest_codechef.csv', 'w', newline='', encoding="utf-8") as f: 
    w = csv.DictWriter(f,['name','date','time']) 
    w.writeheader() 
    for contest in contests: 
        w.writerow(contest) 
