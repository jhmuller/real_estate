import re
import pandas as pd
from bs4 import BeautifulSoup



df = pd.DataFrame.from_csv("realtor.csv", sep="|", encoding="ISO-8859-1")
print(df.head)
print ("done")

dftemp = df
for i, (idx, ser) in enumerate(dftemp.iterrows()):
    html = ser["metaHTML"]
    bs = BeautifulSoup(html)
    for li in bs.find_all("li"):
        temp = li.get("data-label").split('-')
        colname = temp[len(temp)-1]
        if (colname not in df.columns):
            df[colname] = None
        val = li.find("span").text
        df[colname][idx] = val

    colname = "broker"
    html = ser["broker"]
    bs = BeautifulSoup(html)
    if (colname not in df.columns):
        df[colname] = None
    df[colname][idx] = re.sub("Brokered by", '', bs.text)

    html = ser["geo"]
    bs = BeautifulSoup(html)
    elems = bs.find_all("meta")
    for e in elems:
        colname = e.get("itemprop")
        if (colname not in df.columns):
            df[colname] = None
        val = e.get("content")
        df[colname][idx] = val
    print (i)

del df["metaHTML"]
del df["geo"]
print(df.head)
df.to_csv("realtor2.csv", sep="|", quotechar='"',index=False )
print ("done")
