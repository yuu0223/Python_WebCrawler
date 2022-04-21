# Google Comment - Taiwan High Speed Rail
* 透過json解析的方式來爬Google上的評論，之後會再增加文字雲分析的部分！

### Start Coding
> **1. Install The Packages**
```python
from bs4 import BeautifulSoup as bs
import requests
import json
import sys
import pandas as pd
import numpy as np
import re
```
* **bs4套件需先透過終端機去下載**
```
pip install bs4
```
> **2. 將各站的網址存成一個dict**
* 這部分是人工儲存的，還需要再改進！（如果有好的方法都歡迎和我聯繫～）
```python
url_data = {}
url_data['台北'] = '1y3765758547606896641!2y15783762565612593186'
url_data['南港'] = '1y3765760660613716699!2y783023290664905526'
url_data['板橋'] = '1y3765757064874628119!2y8531670796103910821'
#...詳細內容請看完整程式碼
```
> **3. 開始撰寫爬蟲的def**
* **主要是透過for迴圈的方式去換頁爬蟲**
```python
for i in range(10, 510, 10):
            url = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!' + \
                url_data[station]+'!2m2!1i' + \
                str(i)+'!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sjKG4YO74NI_v0AS2zJbADg!7e81'
```

* **將前面設定好的url放進request及json套件中解析**
```python
text = requests.get(url).text

# json格式處理
pretext = ')]}\''
new_text = text.replace(pretext, '')

# 開始爬蟲處理
soup = json.loads(new_text)
conlist = soup[2]
```


