import csv
import requests
import time
import numpy as np

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
        print("Status: Failure While Accessing Rating History for {}".format(username))
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
        print("Status: Failure While Accessing Submission History for {}".format(username))
        return [np.nan] * 4


# Input and output file paths
filename = 'csv/usernames.csv'
output = 'csv/CF_Dataset.csv'
# Format of row: [handle, current_rating, max_rating, n(contest), last 5 rank, last 5 rating, total_correct, overall_accuracy, contest_correct, contest_accuracy]

# Main execution block
with open(filename, 'r') as f:

    usernames = csv.reader(f)
    with open(output, 'a+') as f2:
        w = csv.writer(f2)
        for username_item in usernames:
            username = username_item[0]
            user_info = userinfo(username); time.sleep(0.2)
            if (user_info != None):
                rating_info = userrating_history(username); time.sleep(0.2)
                submission_info = usersubmission_history(username); time.sleep(0.1)
                row = user_info + rating_info + submission_info
                print(row)
                w.writerow(row)
