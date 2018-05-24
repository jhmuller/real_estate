import pandas as pd
import random

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def random_wait(min_secs=1, max_secs=2):
    secs = random.randrange(min_secs, max_secs)
    time.sleep(secs)
    return None

def get_next_page(driver, page):
    try:
        pagination = driver.find_element_by_class_name("pagination")
        if pagination is None:
            return None, driver
        try:
            last = driver.find_element_by_class_name("next-last-page")
        except Exception as lexc:
            msg = "not the last page"
            print (msg)
        else:
            msg = "last page"
            return None, driver
        next_but = driver.find_element_by_class_name("next")
        next_but.click()
        if int(page) > 10:
            msg = "Err there are probably not more than %d pages" % (page,)
            print (msg)
            return None, driver
        return (page + 1, driver)
    except Exception as exc:
        print (exc)
        return None, driver

def do_page(tname, driver, page):
    random_wait(2,4)
    page_list = []
    #rows = driver.find_elements_by_class_name("srp-item-body")
    rows = driver.find_elements_by_class_name("srp-item")
    for i in range(len(rows)):
        row = rows[i]
        random_wait()
        try:
            price = row.find_element_by_class_name("srp-item-price").text
            address = row.find_element_by_class_name("srp-item-address").text

            temp = row.find_element_by_class_name("srp-property-type")
            ptype = temp.get_attribute("innerHTML")

            temp = row.find_element_by_class_name("srp-item-broker")
            broker = temp.get_attribute("innerHTML")

            temp = row.find_element_by_class_name("listing-geo")
            geo = temp.get_attribute("innerHTML")
            try:
                meta = row.find_element_by_class_name("property-meta")
                metaHTML = meta.get_attribute("innerHTML")
                #beds = meta.get_attribute("property-meta-beds")
                #baths = meta.get_attribute("property-meta-bath")
                #sqft = meta.get_attribute("property-meta-sqft")
                #garage = meta.get_attribute("property-meta-garage") or ""
                #lotsz = meta.get_attribute("property-meta-lotsize") or ''
            except Exception as metaExc:
                msg = "No metadata"
                print (msg)
                beds = ''
                baths = ''
                sqft = ''
                lotsz = ''
                garage= ''
            else:
                print ("Metadata!")
        except Exception as exc:
            msg = "Err in town= %s, page=%d" % (tname, page)
            msg += str(exc)
            print (msg)
            continue
        dmap = {"price": price.strip(),
                "broker": broker.strip(),
                "addres": address.strip(),
                "town": tname,
                "geo": geo.strip(),
                "page":page,
                "metaHTML" : metaHTML.strip(),
                "ptype": ptype.strip()}
        print(dmap)
        page_list.append(dmap)
    # now see if there is another page
    return (page_list)

def do_town(tname, driver):
    print(tname)
    random_wait()
    url = "http://www.realtor.com/realestateandhomes-search/%s_MA" % (tname,)
    random_wait()
    town_list = []
    driver.get(url)
    page = 1
    while (page is not None):
        random_wait(2,4)
        page_list = do_page(tname, driver, page)
        town_list += page_list
        random_wait()
        msg = "%s %d listings after %d pages" % (tname, len(town_list), page)
        print(msg)
        page, driver = get_next_page(driver, page)
    return (town_list)

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
            "01776" : "Sudbury",
            "02493": "Weston",
            "01778": "Wayland",
            "02451:": "Waltham",
            "01741": "Carlisle",
            "01890": "Winchester",
            "1754": "Maynard",
            }

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)
all_list = []
towns = list(set(zip2town.values()))
for ti, tname in enumerate(towns):
    town_list = do_town(tname, driver)
    all_list += town_list

df = pd.DataFrame(all_list)
df.to_csv("realtor.csv", sep="|")
print ("done")
