from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()

driver.get('https://www.leetcode.com/contest/')
elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.items-center.leading-\[22px\].dark\:text-dark-label-2 , .lc-md\:text-xl .dark\:group-hover\:text-dark-blue-s'))
    )
i=0
contests=[]
for element in elements:
    if(i==1):
        contest['time']=element.text
        contests.append(contest)
        i=0
        continue
    if(i==0):
        contest={}
        contest['name']=element.text
        i=i+1
with open('csv/contest_leetcode.csv', 'w', newline='', encoding="utf-8") as f: 
    w = csv.DictWriter(f,['time','name']) 
    w.writeheader() 
    for contest in contests: 
        w.writerow(contest) 
