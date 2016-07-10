import urllib2, datetime
from bs4 import BeautifulSoup

donaldTrump = 'realDonaldTrump'
hillaryClinton = 'HillaryClinton'

username = [donaldTrump, hillaryClinton]


#un - Twitter handle
def getTweet(un):
    link = urllib2.urlopen('https://twitter.com/' + un)

    html = link.read()

    soup = BeautifulSoup(html, 'html.parser')

    tweet_text = soup.find_all('div', 'js-tweet-text-container')
    tweet_timestamps = soup.find_all('a', 'tweet-timestamp')
    tweet_links = soup.find_all('a', 'js-details')

    numTweets = len(tweet_text)

    text = [None] * numTweets
    timestamp = [None] * numTweets

    for i in range(0, numTweets):
        text[i] = tweet_text[i].get_text().encode('ascii', 'ignore')
        timestamp[i] = tweet_timestamps[i]['title']
        #link = 'https://twitter.com' + tweet_links[i]['href']

    return text, timestamp

if __name__ == "__main__":
    for un in username:
        print(getTweet(un))