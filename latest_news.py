import time
import notify2
from newsfeed import new_stories
import os


def parse_feed(sleep_interval):
    # path to notification window icon
    ICON_PATH = os.getcwd() + "/icon.ico"

    # fetch news items
    newsitems = new_stories()
    # initialise the d-bus connection
    notify2.init("News Notify")
    # create Notification object
    n = notify2.Notification(None, icon=ICON_PATH)

    for newsitem in newsitems:
        # printing all newsitem on terminal
        print(newsitem['title'])
        print(newsitem['description'])
        print('\n')

        # update notification data for Notification object
        n.update(newsitem['title'], newsitem['description'])
        # set urgency level
        n.set_urgency(notify2.URGENCY_NORMAL)
        # show notification on screen
        n.show()
        # set timeout for a notification
        n.set_timeout(1)
        # short delay between notifications
        time.sleep(sleep_interval)


if __name__ == '__main__':
    try:
        set_interval = int(input("Please enter the interval (in seconds) of news notification: "))
        parse_feed(set_interval)
    except Exception:
        print('\033[91m'+"There's an Error Check your Code \n"+'\033[0m')
        raise
