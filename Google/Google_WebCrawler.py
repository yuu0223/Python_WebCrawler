# Google評論爬蟲

# 套件下載
from bs4 import BeautifulSoup as bs
import requests
import json
import sys
import pandas as pd
import numpy as np
import re

# 各站json名稱
url_data = {}
url_data['台北'] = '1y3765758547606896641!2y15783762565612593186'
url_data['南港'] = '1y3765760660613716699!2y783023290664905526'
url_data['板橋'] = '1y3765757064874628119!2y8531670796103910821'
url_data['桃園'] = '1y3776303546311842201!2y14190658636260526858'
url_data['新竹'] = '1y3776328792349891749!2y17544264445728510275'
url_data['苗栗'] = '1y3776740846221043765!2y2211012256379407514'
url_data['台中'] = '1y3776618627078034237!2y5530670937601927348'
url_data['彰化'] = '1y3776607910030535625!2y1734850936747755733'
url_data['雲林'] = '1y3778151481978021863!2y8988820151700873834'
url_data['嘉義'] = '1y3778126563209183887!2y2411549919517570306'
url_data['台南'] = '1y3778084294240050853!2y161659397133814247'
url_data['左營'] = '1y3777963115452037737!2y2427094121918155174'

# 爬蟲main def


def download_comment():  # 輸入要爬幾筆資料
    author = []
    comment = []
    time = []
    rate = []
    sta = []

    # 選擇車站
    for station in url_data.keys():
        # 選擇要爬幾頁
        for i in range(10, 510, 10):
            url = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!' + \
                url_data[station]+'!2m2!1i' + \
                str(i)+'!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sjKG4YO74NI_v0AS2zJbADg!7e81'

            text = requests.get(url).text

            # json格式處理
            pretext = ')]}\''
            new_text = text.replace(pretext, '')

            # 開始爬蟲處理
            soup = json.loads(new_text)
            conlist = soup[2]

            # 資料存取
            if conlist:
                for data in conlist:
                    com = data[3]
                    if com != None:
                        author.append(str(data[0][1]))
                        comment.append(
                            re.sub('[a-zA-z]+://[^\s]*', '', str(com)))
                        time.append(str(data[1]))
                        rate.append(str(data[4]))
                        sta.append(station)

    # 將爬下來的資料製作成df
    df = pd.DataFrame({'author': author, 'time': time,
                      'comment': comment, 'rate': rate, 'station': sta})

    return df


df = download_comment()
df

# 查看各站評論數量
df.groupby('station').count()

# 存成csv
df.to_csv("高鐵站google評論500則.csv")
