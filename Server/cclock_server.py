from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import requests 
from bs4 import BeautifulSoup 
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

chrome_options = Options()
chrome_options.add_argument("--headless")

def get_CodechefScrap():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.codechef.com/contests/')


    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._data__container_1c9os_464'))
    )

    upcoming_contest=[element.text for element in elements]

    uc={}
    for idx, contest in enumerate(upcoming_contest[:2]):
        split_text=contest.split('\n', 1)
        contest_name=split_text[0]
        info=split_text[1].replace('\n', ' ') if len(split_text)>1 else ''
        uc["Contest{}".format(idx+1)]={'name': contest_name, 'info': info}

    driver.quit()
    return uc

def get_atCoderScrap():
    URL = "https://atcoder.jp/contests/"
    r = requests.get(URL) 
    
    soup = BeautifulSoup(r.content, 'html.parser') 

    table = soup.find('div', attrs = {'id':'contest-table-upcoming'})  
    table2 = table.find('table', attrs = {'class':'table table-default table-striped table-hover table-condensed table-bordered small'})  
    i=0
    count=0
    uc={}
    for row in table2.findAll('tr'):
        contest={}
        for element in row.findAll('td'):
            if(element.a==None):
                continue
            if(i==1):
                contest['name']=element.a.text
                i=0
                continue
            if(i==0):
                contest['time']=element.a.text
                i=i+1
        uc['contest{}'.format(count+1)]=contest
        count=count+1
        if(count==5):
            break
    return uc


def leetCodeScrap():
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.leetcode.com/contest/')
    elements = WebDriverWait(driver, 100).until(
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

    return contests



class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/codeclock':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            response=json.dumps({'Codechef':get_CodechefScrap(), 'Atcoder':get_atCoderScrap(), 'LeetCode': {}})
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
        
if __name__=='__main__':
    server_address=('', 8000)
    httpd=HTTPServer(server_address, RequestHandler)
    print("Server running on http://localhost:8000/")
    httpd.serve_forever()