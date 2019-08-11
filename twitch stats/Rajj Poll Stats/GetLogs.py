import requests as re
from time import sleep

"""Create the URL using the dates from weekend_dates.txt"""
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

# example URL https://overrustlelogs.net/Rajjpatel%20chatlog/April%202019/2019-04-30

# easy way of doing a switch/case, using a dictionary
options = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
urls = []
for entry in dates:
    url = "https://overrustlelogs.net/Rajjpatel%20chatlog/"
    url += options[entry[5:7]] + "%202019/" + str(entry) + ".txt"
    #print(url)
    urls.append(url)
##################################

"""Get the txt file using the urls"""
###################################

for i in range(0,len(urls)):
    print("Retrieving logs from: " + str(urls[i]))
    rr = re.get(urls[i])

    logs = rr.text.split("\n")

    filename = dates[i] + '.txt'
    print("Saving to file: " + filename)

    enc = 'utf-8'
    f = open(filename, 'w+', encoding=enc)

    for entry in logs:
        f.write(entry + '\n')

    f.close()

    sleep(5)

print("Done!")
