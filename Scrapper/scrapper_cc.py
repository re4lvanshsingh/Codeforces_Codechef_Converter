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
        print()

# Main execution block
if __name__ == '__main__':
    username_file = 'csv/usernames.csv'
    output_file = 'csv/CC_Dataset.csv'

    with open(username_file, 'r') as f:
        r = csv.reader(f)

        with open(output_file, 'a+') as f1:
            w = csv.writer(f1)
            for user_item in r:
                username = user_item[0]
                row = extract_content(username)
                print(row)
                w.writerow(row)
                sleep(0.1)  # Controlling the Rate of Requests avoids request failure
