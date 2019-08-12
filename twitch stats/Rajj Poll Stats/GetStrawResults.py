import requests
import AdvancedHTMLParser

def getStats(url):

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

    f = open(filename, 'w')

    if len(usernames) == len(votes):
        #run loop
        for i in range(0,len(votes)):
            f.write(usernames[i] + ',' + votes[i] + '\n')

        f.write(str(total))
    else:
        print('Something wrong')
        exit()

    f.close()

def getUrl():
    x = input('Enter URL or number: ')

    if x[0] == 'h':
        url = x
    elif x.isdigit():
        url = 'https://www.strawpoll.me/' + x + '/r'
    else:
        print('Something wrong')
        exit()


    return url

url = getUrl()
getStats(url)


#print(ct)
