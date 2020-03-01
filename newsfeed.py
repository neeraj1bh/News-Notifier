import requests
import xml.etree.ElementTree as ET

# url of news rss feed you can input any other rss feed as well
RSS_FEED_URL = "http://feeds.bbci.co.uk/news/rss.xml"

# Alternate RSS feed to select from 
# RSS_FEED_URL = "https://www.hindustantimes.com/rss/topnews/rssfeed.xml"    

def load_rss():
    """
    utility function to load RSS feed 
    """
    # create HTTP request response object
    response = requests.get(RSS_FEED_URL)
    # return response content
    return response.content


def parse_xml(rss):
    """
    Utility function to parse XML format rss feed 
    Parses the top news from the BBC RSS news feed and stores it in a list named newslist
    Returns the list "newslist"
    """
    # create element tree root object
    root = ET.fromstring(rss)
    # A list which holds news item in form of dictionary.
    # newslist = [{title:body},{{title:body}}, ........     ]
    newslist = []

    # iterate news items
    for item in root.findall('./channel/item'):
        # create empty dictionary for storing each child in item
        news = {}
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newslist.append(news)

    # return news items list
    return newslist


def new_stories():
    # load rss feed
    rss = load_rss()
    # parse XML
    newsitems = parse_xml(rss)
    return newsitems