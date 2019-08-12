"""Goes through the log files and extracts the strawpoll URLs"""

import re
import requests
import AdvancedHTMLParser

"""Parses the strawpoll page to get the data"""
#################################################
def getStats(url):
    enc = 'utf-8'
    #print(url)

    r = requests.get(url)
    parser = AdvancedHTMLParser.AdvancedHTMLParser()

    parser.parseStr(r.text)

    usernames = []
    votes = []

    txt = parser.getElementsByClassName("option-text")

    for i in range(0,len(txt)):
        usernames.append(txt[i][0].innerText)
        votes.append(txt[i][1].innerText)

    total = 0

    for val in votes:
        total += int(val)

    filename = 'poll results/' + url.split('/')[3] + '.txt'

    f = open(filename, 'w', encoding=enc)

    if len(usernames) == len(votes):
        #run loop
        for i in range(0,len(votes)):
            f.write(usernames[i] + ',' + votes[i] + '\n')

        f.write(str(total))
    else:
        print('Something wrong')
        exit()

    f.close()
#################################################

"""Get dates from weekend_dates.txt"""
################################################
f = open('weekend_dates.txt', 'r')

dates = list(f)

f.close()

date_trim = []
# trim the newline character off
for entry in dates:
    date_trim.append(entry[0:-1])
    #print("The contents are: " + entry)
    #print("The length is: ", len(entry))


dates = date_trim
del(date_trim)
############################################

"""Use the dates to parse the logs for strawpoll urls"""
####################################################
enc = 'utf-8'

for entry in dates:
    filename = "logs/" + entry + ".txt"

    print("Parsing file: ", filename)
    f = open(filename, 'r', encoding=enc)
    text = list(f)
    f.close()

    https = []

    #https://www.strawpoll.me/18458111/r

    for line in text:
        #print(text[i])
        blob = re.search("https://www.strawpoll.me", line)

        if(blob != None):
            line = line.split(' ')

            for word in line:
                if(word[12:21] == "strawpoll"):
                    https.append(word)
        else:
            continue

    # remove duplicates
    list_no_dupes = list(dict.fromkeys(https))

    urlIDs = []

    for url in list_no_dupes:
        match = re.search('\d+', url)
        #print(match.group(0))
        urlIDs.append(match.group(0))

        url = "https://www.strawpoll.me/" + match.group(0) + "/r"
        getStats(url)
#######################################################
