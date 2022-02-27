from bs4 import BeautifulSoup
import requests
import os
from time import time, sleep

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
 
def findPage(URL):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(URL, headers=HEADERS)
 
    soup = BeautifulSoup(webpage.content, "lxml")
 
    try:
        button = soup.find("input",
                          attrs={"id": 'add-to-cart-button'})

        #If button.string doesn't work, means not in stock
        button_name = button.string
            
        notify("Found", "PS5 at Amazon")
    except AttributeError:
        print("Not found: Amazon")
 
if __name__ == '__main__':
    while True:
        findPage("https://www.amazon.com.au/dp/B08HHV8945")
        sleep(60 - time() % 60)