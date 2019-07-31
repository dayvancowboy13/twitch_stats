"""
Made this code obsolete by using Twitch's API
"""

class Retriever:

    def __init__(self):

        # one thing to do: code that takes the standard url and adds number of pages
        # based on user preference
        self.url1 = 'https://twitchtracker.com/channels/live'
        self.url2 = 'https://twitchtracker.com/channels/live?page=2'
        self.usernames = []


    def __del__(self):
        """ Destructor, cleans stuff up"""

        del self.url1, self.url2, self.usernames

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
