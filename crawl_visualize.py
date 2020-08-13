import bs4
import pandas as pd
import requests
import os

url = 'http://www.calendar.ubc.ca/okanagan/index.cfm?tree=18,360,1102,1448'

def crawl(url):
    page = requests.get(url, headers = {"Accept-Language":"en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")

def work(url, path):
    data = crawl(url)

    tit = data.findAll("h2")[0].text.lstrip().rstrip()

    data = data.findAll("table")

    col1 = col2 = pd.Series([])

    for q in range(len(data)):
        
        arr = data[q].findAll("th") + data[q].findAll("td")
        for i in range(len(arr)):
            e = pd.Series([arr[i].text.lstrip().rstrip()])

            if i % 2 == 0:
                col1 = pd.concat([col1, e], ignore_index=True)
            else:
                col2 = pd.concat([col2, e], ignore_index=True)
        df = pd.DataFrame({"INFO": col1, "CREDIT": col2})

        df.to_csv(path + tit + '.csv', index=False)


def prework(url, path):
    data = crawl(url)

    title = data.findAll("h2")[0].text.lstrip().rstrip().replace(" ", '')

    data = data.findAll("table")[0]
    data = data.findAll("a", href=True)
    data = data[::2]

    try:
        os.makedirs(path + title + '/')
    except:
        print("Already exists")
    finally:
        path = path + title + '/'

    for i in range(len(data)):
        data[i] = url.replace(url.replace('http://www.calendar.ubc.ca/okanagan/', ''), data[i]['href'])
        try:
            work(data[i], path)
            print("Done!")
        except:
            print("Failed!")

def pre_prework(url, path):
    data = crawl(url)

    title = data.findAll("h2")[0].text.lstrip().rstrip()

    data = data.findAll("table")[0]
    data = data.findAll("a", href=True)
    data = data[::2]

    try:
        os.makedirs(path + title + '/')
    except:
        print("Already exists")
    finally:
        path = path + title + '/'

    for i in range(len(data)):
        data[i] = url.replace(url.replace('http://www.calendar.ubc.ca/okanagan/', ''), data[i]['href'])
        try:
            prework(data[i], path)
            print("Done!!")
        except:
            print("Failed!!")

def pre_pre_prework():
    url = 'http://www.calendar.ubc.ca/okanagan/index.cfm?tree=18,0,0,0'
    data = crawl(url)
    data = data.findAll("table")[1]
    data = data.findAll("a", href=True)
    data = data[::2]

    path = './okanagan/'

    for i in range(len(data)):
        data[i] = url.replace(url.replace('http://www.calendar.ubc.ca/okanagan/', ''), data[i]['href'])
        try:
            pre_prework(data[i], path)
            print("Done!!!")
        except:
            print("Failed!!!")

pre_pre_prework()