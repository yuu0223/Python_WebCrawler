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
```
url_data = {}
url_data['台北'] = '1y3765758547606896641!2y15783762565612593186'
url_data['南港'] = '1y3765760660613716699!2y783023290664905526'
url_data['板橋'] = '1y3765757064874628119!2y8531670796103910821'
#...詳細內容請看完整程式碼
```
> **3. 開始撰寫**
