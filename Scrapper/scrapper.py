from bs4 import BeautifulSoup
import requests
import json
import re
import csv
import numpy as np
from time import sleep


# Function to extract JSON data from script tag in a specific format
def get_json_from_script_format1(element):
    string = element.string
    json_text = string.split('\n')[2].split(', {')[1].rstrip(');')
    json_text = '{' + json_text
    json_data = json.loads(json_text)
    return json_data

# Function to extract JSON data from script tag in another format
def get_json_from_script_format2(element):
    string = element.string
    pattern = r"name:'(\w+)',y:(\d+),color:"
    matches = re.findall(pattern, string)
    extracted_data = [{'name': match[0], 'number': int(match[1])} for match in matches]
    result = {}
    for data in extracted_data:
        result[data['name']] = data['number']
    return result

# Main function to extract content from a CodeChef user's profile
def extract_content(username):
    url = f'https://www.codechef.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tag = soup.findAll('script', type='text/javascript')
        index = 0
        raw_format_a, raw_format_b = None, None
        for item in script_tag:
            if index == 26:
                raw_format_a = item
            elif index == 28:
                raw_format_b = item
                break
            index += 1

        # Extracting JSON data using the defined functions
        json_a = get_json_from_script_format1(raw_format_a)
        json_b = get_json_from_script_format2(raw_format_b)

        handle = json_a['currentUser']
        contests_list = json_a['date_versus_rating']['all'][::-1]

        rating_list = []
        rank_list = []

        for i in range(min(5, len(contests_list))):
            rating_list.append(contests_list[i]['rating'])
            rank_list.append(contests_list[i]['rank'])

        if len(contests_list) < 5:
            for i in range(5 - len(contests_list)):
                rating_list.append(np.nan)
                rank_list.append(np.nan)

        correct_sub, total_sub = 0, 0
        for item in json_b:
            total_sub += json_b[item]
            if item == 'solutions_accepted':
                correct_sub += json_b[item]

        # Calculating accuracy if there are Submissions
        if total_sub > 0:
            accuracy = round(correct_sub / total_sub, 2)
        else:
            total_sub, accuracy = np.nan, np.nan
        return [handle] + rating_list + rank_list + [correct_sub, accuracy]

    else:
        print(f'Status: Failed to Fetch {username} details')
        return None



# Function to retrieve basic user information from Codeforces API
def userinfo(username):
    url = f'https://codeforces.com/api/user.info?handles={username}'
    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK' and len(data['result']) > 0:
            user = data['result'][0]
            max_rating = user.get('maxRating', 0)
            current_rating = user.get('rating', 0)

            return [user['handle'], current_rating, max_rating]

        else:
            return [np.nan] * 3

    else:
        print('Status: Got Error while Searching {} on Codeforces'.format(username))
        return None


# Function to retrieve user rating history from Codeforces API
def userrating_history(username):
    url = f'https://codeforces.com/api/user.rating?handle={username}'
    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == "OK" and len(data['result']) > 0:

            newdict = list(data['result'])[::-1]

            n_contest = len(data['result'])

            rank_list, rating_list = [], []

            for i in range(min(5, len(newdict))):
                rank_list.append(newdict[i]['rank'])
                rating_list.append(newdict[i]['newRating'])

            if (len(newdict) < 5):
                for j in range(5 - len(newdict)):
                    rank_list.append(np.nan)
                    rating_list.append(np.nan)

            return [n_contest] + rank_list + rating_list

        else:
            return [np.nan] * 11

    else:
        print("Status: Failed to Access Rating History for {}".format(username))
        return [np.nan] * 11


# Function to retrieve user submission history from Codeforces API
def usersubmission_history(username):
    url = f'https://codeforces.com/api/user.status?handle={username}'
    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK' and len(data['result']) > 0:
            right = 0
            total = 0
            contestRight = 0
            contestTotal = 0
            for row in data['result']:
                ptype = row['author']['participantType']
                status = row['verdict']
                total += 1
                if ptype in ['CONTESTANT', 'OUT_OF_COMPETITION']:
                    contestTotal += 1
                    if status == 'OK': contestRight += 1
                if status == 'OK': right += 1

            if (total>0):   accuracy = round(right / total, 2)
            else: accuracy=np.nan
            
            if (contestTotal > 0):  contestAccuracy = round(contestRight / contestTotal, 2)
            else:   contestAccuracy = np.nan

            return [right, accuracy, contestRight, contestAccuracy]

        else:
            return [np.nan] * 4
    else:
        print("Status: Failed to Access Submission History for {}".format(username))
        return [np.nan] * 4


def cross_validator(username):
    cf_user_info = userinfo(username); sleep(0.2)
    if (cf_user_info != None):
        rating_info = userrating_history(username); sleep(0.2)
        submission_info = usersubmission_history(username); sleep(0.2)
        row_CF = cf_user_info + rating_info + submission_info
        row_CC = extract_content(username)
        if row_CC!=None:
            # row_CF=['Handle', 'Current Rating', 'Max Rating', 'Last Five Rating', 'Last Five Contest Rank', 'Overall Correct', 'Overall Accuracy', 'Contest Correct', 'Contest Accuracy']
            # row_CC=['Handle', 'Last Five Rating', 'Last Five Contest Rank', 'Contest Right', 'Contest Accuracy']
            return row_CF+row_CC[1:]
        else: return None

# Main execution block
if __name__ == '__main__':
    username_file = 'csv/usernames.csv'
    output_file = 'csv/ratings.csv'
    usernames=[]
    with open(username_file, 'r') as f:
        r = csv.reader(f)
        usernames=list(r)
    
    total_users=len(usernames)
    counter=0
    success=0
    print(f"Starting Scrapper: {len(usernames)} users in Stack.")
    with open(output_file, 'a+') as f1:
        w = csv.writer(f1)
        for user_item in usernames:
            username=user_item[0]
            counter+=1
            row = cross_validator(username)
            if row!=None:
                success+=1
                print(f"({success}/{counter}) Passed, Total: {total_users}", end='   ')
                print(row[0:3], end='...\n')
                w.writerow(row)
                sleep(0.1)  # Controlling the Rate of Requests avoids request failure
