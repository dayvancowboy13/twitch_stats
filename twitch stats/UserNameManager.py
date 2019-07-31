## This code will gather user names for the main data pulling code.

import requests
from datetime import date

#adding random comment

## Kinda clunky way of getting usernames: using the site www.twitchtracker.com,
## it pulls the streamers in the top 20 current live viewers.

class Retriever:

    def __init__(self):

        # one thing to do: code that takes the standard url and adds number of pages
        # based on user preference
        self.url1 = 'https://twitchtracker.com/channels/live'
        self.url2 = 'https://twitchtracker.com/channels/live?page=2'
        self.usernames = []


    def __del__(self):
        """ Destructor, cleans stuff up"""

        #print("Goodbye :(")

    def get_html(self, url):

        r = requests.get(url)

        ss = r.text
        html_lines = ss.split('\n')

        return html_lines

    def get_usernames(self, html_lines):
        usernames = []
        count = 0

        for line in html_lines:

            if line == '<div class="ri-name">':

                # sample of the line text to expect: <a href="/destiny">Destiny</a>
                nextLine = html_lines[count+1]
                # the following trims off the a href tags
                nextLine_trim = nextLine[10:-4]

                # copy characters from the string until the " is reached
                username = ''

                for i in range(0,len(nextLine_trim)):
                    if nextLine_trim[i] == "\"":
                        break
                    else:
                        username += nextLine_trim[i]

                usernames.append(username)

            count += 1

        return usernames
def write_names_to_file(uNames):

    f = open('tempnames.txt', 'w')

    for name in uNames:
        f.write(name + "\n")

    f.close()

#def check_sub_data(uNames):


# get usernames from file
f = open('usernames.txt', 'r')

existing_uNames = list(f)

f.close()

# this code removes the '\n' at the end of each list item
count = 0
for name in existing_uNames:
    name = name[0:-1]
    #print(name)
    existing_uNames[count] = name
    count += 1

rr = Retriever()

html = rr.get_html(rr.url1)
rr.usernames = rr.get_usernames(html)
html = rr.get_html(rr.url2)
rr.usernames += rr.get_usernames(html)

combined_usernames = rr.usernames + existing_uNames

# very compact code for clearing out duplicates
list_no_dupes = list(dict.fromkeys(combined_usernames))

### CHECK THE LIST OF NO DUPES FOR STREAMERS ON THE NOSUBDATA LIST HERE ###

write_names_to_file(list_no_dupes)
