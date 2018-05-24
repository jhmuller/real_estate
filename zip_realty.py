import pandas as pd
import random

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()

zip2town = {"01742" : "Concord",
            "01718" : "Acton",
            "01719" : "Acton",
            "02474" : "Arlington",
            "02475": "Arlington",
            "02476": "Arlington",
            "01730": "Bedford",
            "01731": "Bedford",
            "02479": "Belmont",
            "02420": "Lexington",
            "02421": "Lexington",
            "01773": "Lincon",
            "01776" : "Sudbury"
            }


do_town(tname, tzip):

process_page(driver):

def random_wait(min_secs=1, max_secs=2):
    secs = random.randrange(min_secs, max_secs)
    time.sleep(secs)
    return None

dlist = []
verbose=True
page = 1
towns = set()
while page is not None:
for tzip, tname in zip2town.items():

    zzip = tzip+'z'
    url = "http://www.ziprealty.com/for-sale-homes/%s/view_map?src=view" % (zzip,)
    url = "http://www.zillow.com/%s-ma/" % (tname.lower(),)
    #url = "http://www.realtor.com/realestateandhomes-search/%s_MA" % (tname,)
    random_wait()
    driver.get(url)
    random_wait()
    rows = driver.find_elements_by_class_name("photo-card")
    if verbose:
        msg = "town= %s, zip=%s" % (tname, tzip)
        msg += "# rows= %d" % (len(rows),)
        print(msg)

    for i in range(len(rows)):
        row = rows[i]
        random_wait()
        print(row.text)
        random_wait()
        ltext = row.text
        if len(ltext) < 10:
            msg = "Err in town= %s, zip=%s" % (tname, tzip)
            msg += " no listing for listing=%s" % (ltext,)
            print(msg)
            continue
        else:
            dmap = {"text": ltext,
                "town": tname,
                "zip" : tzip}
            dlist.append(dmap)
            print(dmap)
            print ("here")
df = pd.DataFrame(dlist)
df.to_csv("zipRealty.csv")
print ("done")







rows = driver.find_elements_by_class_name("home-results-list")

rows = driver.find_elements_by_class_name("media__content")

rows[0].text

brokers = driver.find_elements_by_class_name("cf")
