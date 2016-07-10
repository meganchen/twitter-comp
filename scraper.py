import urllib2, datetime
from bs4 import BeautifulSoup

donaldTrump = 'realDonaldTrump'
hillaryClinton = 'HillaryClinton'

username = [donaldTrump, hillaryClinton]

link = urllib2.urlopen('https://twitter.com/' + username[1])

html = link.read()

soup = BeautifulSoup(html, 'html.parser')

tweet_text = soup.find_all('div', 'js-tweet-text-container')
tweet_timestamps = soup.find_all('a', 'tweet-timestamp')
tweet_links = soup.find_all('a', 'js-details')

for i in range(0, len(tweet_text)):
    text = tweet_text[i].get_text().encode('ascii', 'ignore')
    print(text)
    #timestamp = datetime.datetime.strptime(tweet_timestamps[i]['data-original-title'], '%I:%M %p - %d %b %y')
    print(tweet_timestamps[i]['title'])
    #link = 'https://twitter.com' + tweet_links[i]['href']