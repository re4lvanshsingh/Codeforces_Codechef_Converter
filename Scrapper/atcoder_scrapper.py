import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "https://atcoder.jp/contests/"
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html5lib') 
contests=[]

table = soup.find('div', attrs = {'id':'contest-table-upcoming'})  
table2 = table.find('table', attrs = {'class':'table table-default table-striped table-hover table-condensed table-bordered small'})  
i=0
count=0
for row in table2.findAll('tr'):
    for element in row.findAll('td'):
        if(element.a==None):
            continue
        if(i==1):
            contest['name']=element.a.text
            contests.append(contest)
            i=0
            continue
        if(i==0):
            contest={}
            contest['time']=element.a.text
            i=i+1
    count=count+1
    if(count==5):
        break
with open('csv/contest_atcoder.csv', 'w', newline='', encoding="utf-8") as f: 
    w = csv.DictWriter(f,['time','name']) 
    w.writeheader() 
    for contest in contests: 
        w.writerow(contest) 
