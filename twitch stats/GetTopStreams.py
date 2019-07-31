import requests
import json

def get_top_streams(num_entries):

    # call this function from other python file, send the number of number
    # of entries to retrieve

    url = 'https://api.twitch.tv/helix/streams?first=' + str(num_entries)

    # send my request
    r = requests.get(url, headers={'Client-ID':'1eqrgf88jl70th3jnvrju7g95cqfiz'})

    info_dict = json.loads(r.text)

    moreinfo = info_dict['data']

    usernames = []

    for item in moreinfo:
        # add the names to the usernames list
        usernames.append(item['user_name'].lower())

    f = open('tempnames.txt', 'w')

    count = 0

    for name in usernames:
        # try writing, if there's any error just skip it
        try:
            f.write(name + '\n')
            count += 1
        except:
            print('Failed to add username')
            continue

    print('Added %d / %d streamers' % (count,num_entries))

    f.close()
