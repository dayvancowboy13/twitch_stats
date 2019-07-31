## This code will gather user names for the main data pulling code.

import requests
from datetime import date
from GetTopStreams import get_top_streams
from Retriever import Retriever

## Kinda clunky way of getting usernames: using the site www.twitchtracker.com,
## it pulls the streamers in the top 20 current live viewers.


def write_names_to_file(uNames):
"""Write the names in uNames to a file."""
    f = open('tempnames.txt', 'w')

    for name in uNames:
        f.write(name + "\n")

    f.close()

# get usernames from file
f = open('usernames.txt', 'r')

existing_uNames = list(f)

f.close()

## this code removes the '\n' at the end of each list item
count = 0
for name in existing_uNames:
    name = name[0:-1]
    #print(name)
    existing_uNames[count] = name
    count += 1
##

retriever = Retriever()

html = retriever.get_html(retriever.url1)
retriever.usernames = retriever.get_usernames(html)
html = retriever.get_html(retriever.url2)
retriever.usernames += retriever.get_usernames(html)

combined_usernames = retriever.usernames + existing_uNames

# very compact code for clearing out duplicates
list_no_dupes = list(dict.fromkeys(combined_usernames))

### CHECK THE LIST OF NO DUPES FOR STREAMERS ON THE NOSUBDATA LIST HERE ###

write_names_to_file(list_no_dupes)

get_top_streams(20)
